from .models import Users
from .models import Subject
from rest_framework_mongoengine import serializers 
from rest_framework_mongoengine.serializers import DocumentSerializer,EmbeddedDocumentSerializer

class SubjectSerializer(DocumentSerializer):  
    class Meta:
        model = Subject
        fields = ['id','sub_name','sub_duration']
        extra_kwargs = {
            'name' : {
                'sub_name' : False
            },
            'marks' : {
                'sub_duration' : False
            }
        }

class UserSerializer(DocumentSerializer):
    subject = SubjectSerializer(required=False,many = True)
    class Meta:
        model = Users
        fields = ['id','name','marks','subject']
        extra_kwargs = {
            'name' : {
                'required' : True
            },
            'marks' : {
                'required' : True
            },
            'subject' : {
                'required' : False
            }
        }

# class Subject_Data(serializers.DocumentSerializer):
#     class Meta:
#         model = SubjectData
#         fields = ['id','sub_name','sub_duration']