# from .models import Users, Subject
# from rest_framework_mongoengine.serializers import DocumentSerializer
from mongoengine import Document


class MyCustomField(Document):
    def __init__(self,data):
        print("hello")
        print(data)