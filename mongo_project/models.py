from django.db import models
from mongoengine import *
from datetime import *
# from .custom_field import MyCustomField

class Subject(Document):
    sub_name = StringField(required = True, max_length=50)
    sub_duration = IntField(required = True)
    created_on = DateTimeField(default = datetime.utcnow)

class Users(Document):
    name = StringField(required = True, max_length=50)
    marks = IntField(required = True)
    email = EmailField(required = True, allow_ip_domain = True, allow_utf8_user = True)
    age = IntField(max_value = 100, min_value = 1)
    subject = ListField(ReferenceField('Subject'))
    # subject = ListField(StringField())
    # subject = ListField(EmbeddedDocumentField(Subject))
    # subject = ListField(MyCustomField(Subject))
    created_on = DateTimeField(default = datetime.utcnow)





