# coding=utf-8
from flask import Flask
from flask import render_template

from power.config import DefaultConfig
from power.config import INSTANCE_FOLDER_PATH
from power.frontend import frontend
from power.admin import admin

from power.extensions import db, login_manager, cache

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
    app.config.from_pyfile('production.cfg', silent=True)
    if config:
        app.config.from_object(config)


def configure_extensions(app):
    db.init_app(app)

    # flask-cache
    cache.init_app(app)

    # flask-login
    login_manager.login_view = 'frontend.login'
    #login_manager.refresh_view = 'frontend.reauth'

    login_manager.setup_app(app)


def config_error_handlers(app):
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/404.html")

    @app.errorhandler(403)
    def forbidden(error):
        return render_template("errors/403.html")
