# -*- coding: utf-8 -*-
from power.extensions import db


class Role(db.Document):
    name = db.StringField(required=True, primary_key=True)
    git_repo = db.StringField(max_length=50)
    auto_update = db.StringField(max_length=50)