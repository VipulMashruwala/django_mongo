from .models import Users, Subject
from rest_framework_mongoengine.serializers import DocumentSerializer
# from rest_framework_mongoengine import serializers
from rest_framework import serializers
from mongoengine import *

class SubjectSerializer(DocumentSerializer):  
    class Meta:
        model = Subject
        fields = ['id','sub_name','sub_duration','created_on']

    #     extra_kwargs = {
    #     'sub_name' : {
    #         'required' : True
    #     },
    #     'sub_duration' : {
    #         'required' : True
    #     }
    # }

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
        fields = ['id','name','marks','email','age','subject','created_on']
        # extra_kwargs = {
        #     'name' : {
        #         'required' : True
        #     },
        #     'marks' : {
        #         'required' : True
        #     },
        #     'subject' : {
        #         'required' : False
        #     }
        # }