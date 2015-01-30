# coding=utf-8
#!/usr/bin/python

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'OPTIONS'])
def hello_world():
    return render_template('index.html')

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return 'Hello World'

@app.route('/roles', methods=['GET', 'POST'])
def show_roles():
    # show the user profile for that user
    return "platform roles"

@app.route('/roles/<uuid>', methods=['GET', 'POST'])
def show_role(uuid):
    return "platform roles {0}".format(uuid)

@app.route('/hosts', methods=['GET', 'POST'])
@app.route('/hosts/<uuid>', methods=['GET', 'POST'])
def show_hosts(uuid=None):
    if uuid:
        return "platform host {0}".format(uuid)
    return "platform roles"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)