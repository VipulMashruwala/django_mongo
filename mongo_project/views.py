from django.views.generic import View
from .models import Users, Subject
from .serializers import UserSerializer, SubjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class UserListCBV(APIView):
    def get(self, request):
        id = request.data.get('id',None)
        if id is not None:
            try:
                user = Users.objects.get(id = id)
            except Users.DoesNotExist:
                return Response({'msg': 'user not exists'})

            serializer = UserSerializer(user)
            return Response(serializer.data, content_type = 'application/json')
        
        users = Users.objects.all()
        serializer = UserSerializer(users,many = True)
        print(serializer.data)
        return Response(serializer.data, content_type = 'application/json')
       
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'user created successfully'})
        return Response(serializer.errors)

    def put(self, request):
        data = json.loads(request.body)
        id = data.get('id')
        try:
            user = Users.objects(id = id)
        except Users.DoesNotExist:
            return Response({'msg': 'user not exists'})

        name = data.get('name',None)
        if name is not None:
            user.update_one(set__name = name)

        marks = data.get('marks')
        if marks is not None:
            user.update_one(set__marks = marks)
        
        subject = data.get('subject')
        if subject is not None:
            user.update_one(add_to_set__subject = subject)

        return Response({'msg' : 'user updated successfully'})

    def delete(self,request):
        data = json.loads(request.body)
        id = data.get('id')
        try:
            user = Users.objects(id = id)
        except Users.DoesNotExist:
            return Response({'msg':'user not exists'})

        subject = data.get('subject',None)
        if subject is not None and len(subject) > 0:
            user.update_one(pull_all__subject = subject)
            return Response({'msg' : 'subject deleted successfully'})
        else:
            user.delete()
            return Response({'msg' : 'user deleted successfully'})

class SubjectListCBV(APIView):
    def get(self, request):
        id = request.data.get('id',None)
        if id is not None:
            try:
                sub = Subject.objects.get(id = id)
            except Subject.DoesNotExist:
                return Response({'msg': 'subject not exists'})
            
            serializer = SubjectSerializer(sub)
            return Response(serializer.data, content_type = 'application/json')
        
        subs = Subject.objects.all()
        serializer = SubjectSerializer(subs,many = True)
        return Response(serializer.data, content_type = 'application/json')
       
    def post(self, request):
        serializer = SubjectSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'subject created successfully'})
        return Response(serializer.errors)
