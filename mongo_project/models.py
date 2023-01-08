from django.db import models
from mongoengine import *
from datetime import *

class Subject(Document):
    sub_name = StringField(required = True, max_length=50)
    sub_duration = IntField(required = True)
    created_on = DateTimeField(default = datetime.utcnow)

class Users(Document):
    name = StringField(required = True, max_length=50)
    marks = IntField(required = True)
    email = EmailField(required = True, allow_ip_domain = True, allow_utf8_user = True)
    age = IntField(max_value = 100, min_value = 1)
    subject = ListField(ReferenceField(Subject, required = False))
    created_on = DateTimeField(default = datetime.utcnow)

class CreateUser(Document):
    username = StringField(required = True, max_length=50)
    password = StringField(required = True, max_length= 12)
    is_admin = BooleanField(required = False, default = False)
    user_data = ReferenceField(Users)
    is_login = BooleanField(required = False, default = False)
    created_on = DateTimeField(default = datetime.utcnow)


