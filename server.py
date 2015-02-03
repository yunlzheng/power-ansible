# coding=utf-8
# !/usr/bin/python
import os.path
from flask import Flask
from flask import render_template

from power.api.demo import DemoAPI

app = Flask(__name__)
app.add_url_rule('/api/demo', view_func=DemoAPI.as_view('demos'))


@app.route('/', methods=['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'OPTIONS'])
def hello_world():
    return render_template('index.html')


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return 'Hello World'


@app.route('/roles', methods=['GET', 'POST'])
@app.route('/roles/<uuid>', methods=['GET', 'POST'])
def roles(uuid=None):
    if uuid:
        return "platform host {0}".format(uuid)
    return render_template('roles.html')


@app.route('/hosts', methods=['GET', 'POST'])
@app.route('/hosts/<uuid>', methods=['GET', 'POST'])
def show_hosts(uuid=None):
    if uuid:
        return "platform host {0}".format(uuid)
    return render_template('hosts.html')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)