# -*- coding: utf-8 -*-

from wtforms.form import Form
from wtforms import (ValidationError, HiddenField, BooleanField, TextField,
                            PasswordField, SubmitField, StringField)
from wtforms import validators


class LoginForm(Form):
    next = HiddenField()
    login = StringField(u'Username or email', [validators.input_required()])
    password = PasswordField(u'Password', validators=[validators.input_required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign in')

if __name__ == "__main__":
    form = LoginForm()
    for field in form:
        print field.label.__dict__
#print form.__dict__