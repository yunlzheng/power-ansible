# coding=utf-8
import os
from bson.objectid import ObjectId
from flask import (Flask, current_app)
from flask import render_template
from flask.ext.assets import Bundle
import pymongo

from power.config import DefaultConfig
from power.config import INSTANCE_FOLDER_PATH
from power.frontend import frontend
from power.admin import admin
from power.user.modles import User

from power.extensions import db, login_manager, cache, debug_toolbar, assets

__all__ = ['create_app']

DEFAULT_BLUEPRINTS = (
    frontend,
    admin
)


def create_app(config=None, app_name=None, blueprints=None):
    if app_name is None:
        app_name = DefaultConfig.PROJECT
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS

    app = Flask(app_name, instance_path=INSTANCE_FOLDER_PATH, instance_relative_config=True)
    configure_app(app, config)
    register_blueprints(app, blueprints)
    config_error_handlers(app)
    configure_extensions(app)
    return app


def register_blueprints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_app(app, config=None):
    app.config.from_object(DefaultConfig)
    app.logger.debug(DefaultConfig.DEBUG)
    app.config.from_pyfile('production.cfg', silent=True)
    app.debug = True
    if config:
        app.config.from_object(config)


def configure_extensions(app):
    db.init_app(app)
    # flask-cache
    cache.init_app(app)

    # flask-login
    login_manager.login_view = 'frontend.login'
    # login_manager.refresh_view = 'frontend.reauth'

    @login_manager.user_loader
    def load_user(id):
        current_app.logger.debug(id)
        return User.objects.get(email=id)

    login_manager.setup_app(app)
    debug_toolbar.init_app(app)
    assets.init_app(app)
    scss = Bundle('css/scss/*.scss', filters='pyscss', output='css/power.css')
    common_css = Bundle('css/commons/*.css', output='css/commons.css')
    common_ie8_css = Bundle('css/commons/*.css', output='css/commons-ie8.css')
    common_js = Bundle('js/commons/*.js', filters='jsmin', output='js/commons.js')

    assets.register('scss_all', scss)
    assets.register('common-css', common_css)
    assets.register('common-css-ie8', common_ie8_css)
    assets.register('common-js', common_js)


def configure_logging(app):
    if app.debug or app.testing:
        # Skip debug and test mode. Just check standard output.
        return
    import logging
    from logging.handlers import SMTPHandler

    # Set info level on logger, which might be overwritten by handers.
    # Suppress DEBUG messages.
    app.logger.setLevel(logging.INFO)

    info_log = os.path.join(app.config['LOG_FOLDER'], 'info.log')
    info_file_handler = logging.handlers.RotatingFileHandler(info_log, maxBytes=100000, backupCount=10)
    info_file_handler.setLevel(logging.INFO)
    info_file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]')
    )
    app.logger.addHandler(info_file_handler)


def config_error_handlers(app):
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/404.html")

    @app.errorhandler(403)
    def forbidden(error):
        return render_template("errors/403.html")
