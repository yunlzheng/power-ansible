# -*- coding: utf-8 -*-

from wtforms.form import Form
from wtforms.fields import StringField
from wtforms import validators


class LoginForm(Form):
    email = StringField(u'Email', validators=[validators.input_required()])
    password = StringField(u'Password', validators=[validators.input_required()])