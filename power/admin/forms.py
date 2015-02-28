# -*- coding: utf-8 -*-

from wtforms.form import Form

from wtforms.form import Form
from wtforms import (BooleanField, StringField, SelectField, SubmitField)


class CloneRoleForm(Form):
    name = StringField(u'Role Name')
    git_repo = StringField(u'Git Repository URI')
    auto_update = BooleanField(u'Auto Update The Role')


class CreateCredentialForm(Form):

    choices = [('machine','Machine'), ('scm','Source Control'), ('aws','Amazon Web Service'), ('openstack','OpenStack')]

    name = StringField(u'Name')
    description = StringField(u'Description')
    type = SelectField(u'Type', coerce="Chose a type",
                       choices=choices, id="type")
    machine_ssh_username = StringField("SSH Username")
    machine_ssh_password = StringField("SSH Password")
    machine_confirm_ssh_password = StringField('Confirm SSH Password')
    machine_ssh_private_key = StringField('SSH Private Key')
    machine_key_password = StringField('Key Password')

    scm_username = StringField('Username')
    scm_password = StringField('Password')
    scm_private_key = StringField('SCM Private Key')
    scm_key_password = StringField('SCM Key Password')

    aws_access_key = StringField("Access Key")
    aws_secret_key = StringField('Secret Key')

    openstack_auth_url = StringField("Auth URL")
    openstack_access_key = StringField("Access Key")
    openstack_secret_key = StringField('Secret Key')

    submit = SubmitField('Save')
