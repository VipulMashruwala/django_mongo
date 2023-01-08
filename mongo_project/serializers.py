from .models import Users, Subject, CreateUser
from rest_framework_mongoengine.serializers import DocumentSerializer
# from rest_framework_mongoengine import serializers
from rest_framework import serializers
from mongoengine import *

class SubjectSerializer(DocumentSerializer):  
    class Meta:
        model = Subject
        fields = ['sub_name','sub_duration','created_on']

class UserSerializer(DocumentSerializer):
    subject = SubjectSerializer(required = False,many = True,
    read_only = True)
    
    def validate_marks(self,data):
        if data < 33:
            raise serializers.ValidationError('Fail')
        return data
             
    def validate_email(self,data):
        d = data.split('@')
        if d[-1] not in ["nmims.edu","outlook.com","gmail.com"]:
            raise serializers.ValidationError("Invalid Email")
        return data

    class Meta:
        model = Users
        fields = ['name','marks','email','age','subject','created_on']

class CreateUserSerializer(DocumentSerializer):
    user_data = UserSerializer(required = False)
    class Meta:
        model = CreateUser
        fields = ['id','username','password','is_admin','is_login','created_on','user_data']

    