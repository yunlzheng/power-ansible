# -*- coding: utf-8 -*-

from wtforms.form import Form

from wtforms.form import Form
from wtforms import (BooleanField, StringField)


class CloneRoleForm(Form):
    name = StringField(u'Role Name')
    git_repo = StringField(u'Git Repository URI')
    auto_update = BooleanField(u'Auto Update The Role')