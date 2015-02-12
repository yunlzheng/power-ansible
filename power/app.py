# coding=utf-8
from flask import Flask
from flask import render_template

from power.config import DefaultConfig
from power.config import INSTANCE_FOLDER_PATH
from power.frontend import frontend
from power.admin import admin

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
    return app


def register_blueprints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_app(app, config=None):
    app.config.from_object(DefaultConfig)
    app.config.from_pyfile('production.cfg', silent=True)
    if config:
        app.config.from_object(config)


def config_error_handlers(app):
    @app.errorhandler(404)
    def page_not_found():
        return render_template("errors/404.html")

    @app.errorhandler(403)
    def forbidden():
        return render_template("errors/403.html")
