# -*- coding: utf-8 -*-

import flask.ext

from flask.ext.mongoengine import MongoEngine
db = MongoEngine()

# from flask.ext.mail import Mail
# mail = Mail()

from flask.ext.cache import Cache
cache = Cache()

from flask.ext.login import LoginManager
login_manager = LoginManager()

from flask_debugtoolbar import DebugToolbarExtension

debug_toolbar = DebugToolbarExtension()
