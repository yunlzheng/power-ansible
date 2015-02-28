# -*- coding: utf-8 -*-

from flask import (Blueprint, render_template, request,
                   flash, url_for, redirect, current_app)

from flask.ext.login import login_required, login_user, current_user, logout_user, confirm_login, login_fresh
from power.frontend.forms import LoginForm
from power.user.modles import User

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def index():
    return render_template('index.html')


@frontend.route('/login', methods=["get", "post"])
def login():
    if current_user.is_authenticated():
        return redirect(url_for('admin.index'))

    form = LoginForm(request.form)

    if form.validate():
        user, authenticated = User.authenticate(form.login.data, form.password.data)
        if user and authenticated:
            remember = request.form.get('remember') == 'y'
            if login_user(user, remember=remember):
                flash("Logged in", 'success')
            return redirect(form.next.data or url_for('admin.index'))
        else:
            flash('Sorry, invalid login', 'error')
    return render_template('frontend/login.html', form=form)


@frontend.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('frontend.index'))