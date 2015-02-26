# -*- coding: utf-8 -*-

from flask import (Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort)

from flask.ext.login import login_required

from power.ui.projects_adaptor import ProjectsAdaptor
from power.admin.forms import CloneRoleForm
from power.common.git import Git

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/')
@login_required
def index():
    return render_template('admin/dashboard.html')


@admin.route('/roles')
@admin.route('/roles/<int:uuid>')
@login_required
def roles(uuid=None):
    if uuid:
        return render_template('admin/role.html')
    return render_template('admin/roles.html')

@admin.route('/roles/clone', methods=['GET', 'POST'])
def download_role():
    form = CloneRoleForm(request.form)
    if form.validate():
        Git.clone(form.name, form.git_repo)


@admin.route('/roles/add', methods=['GET'])
@login_required
def add_role():
    return render_template("admin/add_roles.html")


@admin.route('/tasks', methods=['GET', 'POST'])
@admin.route('/tasks/<uuid>', methods=['GET', 'POST'])
@login_required
def tasks(uuid=None):
    if uuid:
        return "platform tasks {0}".format(uuid)
    return render_template('admin/tasks.html')


@admin.route('/hosts', methods=['GET', 'POST'])
@admin.route('/hosts/<uuid>', methods=['GET', 'POST'])
@login_required
def hosts(uuid=None):
    if uuid:
        return "platform host {0}".format(uuid)
    return render_template('admin/hosts.html')


@admin.route('/projects')
@admin.route('/projects/<uuid>')
@login_required
def projects(uuid=None):
    return ProjectsAdaptor(request, uuid=uuid).handle()

