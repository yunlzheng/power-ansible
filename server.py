# coding=utf-8
# !/usr/bin/python
import os.path
from flask import Flask
from flask import render_template
from flask import request, redirect

from power.api.demo import DemoAPI
from power.ui.projects_adaptor import ProjectsAdaptor

app = Flask(__name__)
app.add_url_rule('/api/demo', view_func=DemoAPI.as_view('demos'))


@app.route('/', methods=['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'OPTIONS'])
def hello_world():
    return render_template('index.html')

@app.route('/admin', methods=['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'OPTIONS'])
def dashboard():
    return render_template('admin/dashboard.html')


@app.route('/admin/roles', methods=['GET', 'POST'])
@app.route('/admin/roles/<uuid>', methods=['GET', 'POST'])
def roles(uuid=None):
    if uuid:
        return "platform host {0}".format(uuid)
    return render_template('admin/roles.html')

@app.route('/admin/tasks', methods=['GET', 'POST'])
@app.route('/admin/tasks/<uuid>', methods=['GET', 'POST'])
def tasks(uuid=None):
    if uuid:
        return "platform tasks {0}".format(uuid)
    return render_template('admin/tasks.html')

@app.route('/admin/hosts', methods=['GET', 'POST'])
@app.route('/admin/hosts/<uuid>', methods=['GET', 'POST'])
def hosts(uuid=None):
    if uuid:
        return "platform host {0}".format(uuid)
    return render_template('admin/hosts.html')

@app.route('/admin/projects')
@app.route('/admin/projects/<uuid>')
def projects(uuid=None):
    return ProjectsAdaptor(request, uuid=uuid).handle()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        return redirect("/admin")
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    return redirect("/")

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)