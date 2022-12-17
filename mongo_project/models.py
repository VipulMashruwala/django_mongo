from django.db import models
from mongoengine import *

# Create your models here.

# class SubjectData(EmbeddedDocument):
#     sub_name = StringField()
#     sub_duration = IntField()

class Subject(Document):
    sub_name = StringField(required = True, max_length=50)
    sub_duration = IntField(required = True)


class Users(Document):
    name = StringField(required = True, max_length=50)
    marks = IntField(required = True)
    subject = ListField(ReferenceField(Subject))




