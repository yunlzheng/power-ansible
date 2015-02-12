# -*- coding: utf-8 -*-

from flask import (Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort)

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def index():
    return render_template('index.html')


@frontend.route('/login', methods=["get", "post"])
def login():
    if request.method == "POST":
        return redirect("/admin")
    else:
        return render_template('frontend/login.html')


@frontend.route('/logout')
def logout():
    return redirect("/")