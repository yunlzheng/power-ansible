# -*- coding: utf-8 -*-
from bson.objectid import ObjectId
from flask import current_app
from power.extensions import db


class User(db.Document):
    email = db.StringField(required=True, primary_key=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    created_time = db.DateTimeField()
    avatar = db.StringField()
    password = db.StringField()

    def check_password(self, password):
        if self.password is None:
            return False
        return self.password == password

    def get_id(self):
        return str(self.id)

    def is_active(self):
        # TODO: User is active or just ignore?
        return True

    def is_authenticated(self):
        return True

    @classmethod
    def get_by_id(cls, user_id):
        current_app.logger.debug("User.get_by_id({0})".format(user_id))
        return cls.objects.first()

    @classmethod
    def authenticate(cls, login, password):
        user = User.objects(email=login).first()
        if user:
            authenticated = user.check_password(password)
        else:
            authenticated = False
        return user, authenticated

