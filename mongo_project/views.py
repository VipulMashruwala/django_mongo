from django.views.generic import View
from .models import Users, Subject, CreateUser
from .serializers import UserSerializer, SubjectSerializer, CreateUserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.exceptions import ValidationError
from rest_framework.authentication import SessionAuthentication
from .custom_permission import CustomPermission,CustomPermissionSubject, CustomPermissionLogout, CustomPermissionUser
from .utils import IsAdmin

@method_decorator(csrf_exempt, name='dispatch')
class UserListCBV(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [CustomPermissionUser]

    def get(self, request):
        id = request.data.get('user_id',None)
        if id is not None:
            try:
                user = Users.objects.get(id = id)
            except Users.DoesNotExist:
                return Response({'msg': 'user not exists'})

            serializer = UserSerializer(user)
            return Response(serializer.data, content_type = 'applic/ation/json')
        
        users = Users.objects.all()
        serializer = UserSerializer(users,many = True)
        return Response(serializer.data, content_type = 'application/json')
       
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        print(request.data)
        if serializer.is_valid():
            req_data = request.data
            user = Users(name = req_data['name'],
                    marks = req_data['marks'],
                    email = req_data['email'],
                    age = req_data['age'],
                    subject = req_data['subject'])
            user.save()    
            create_user = CreateUser.objects.get(id = request.data['id'])
            create_user.update(set__user_data = user["id"])
            return Response({'msg' : 'user created successfully'})
        else:
            return Response(serializer.errors)

    def put(self, request):
        id = request.data.get('user_id')
        try:
            user = Users.objects.get(id = id)
        except Users.DoesNotExist:
            return Response({'msg': 'user not exists'})

        name =  request.data.get('name',None)
        if name is not None:
            user.update(set__name = name)

        marks =  request.data.get('marks')
        if marks is not None:
            user.update(set__marks = marks)

        email = request.data.get('email')
        if email is not None:
            user.update(set__email = email)

        age = request.data.get('age')
        if age is not None:
            user.update(set__age = age)
        
        subject =  request.data.get('subject')
        if subject is not None:
            user.update(add_to_set__subject = subject)

        return Response({'msg' : 'user updated successfully'})
    
    def delete(self,request):
        id = request.data.get('user_id')
        try:
            user = Users.objects.get(id = id)
        except Users.DoesNotExist:
            return Response({'msg':'user not exists'})
        
        subject = request.data.get('subject',None)
        if subject is not None and len(subject) > 0:
            user.update(pull_all__subject = subject)
            return Response({'msg' : 'subject deleted successfully'})
        else:
            create_user = CreateUser.objects.get(id = request.data['id'])
            create_user.update(set__user_data = None)
            user.delete()
            return Response({'msg' : 'user deleted successfully'})

class SubjectListCBV(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [CustomPermissionSubject]
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

class CreateUserList(APIView):
    def post(self, request):
        print(request.data)
        serializer = CreateUserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class LoginUser(APIView):
    def post(self,request):
        username = request.headers['username']
        password = request.headers['password']        
        try:
            user_data = CreateUser.objects.get(username = username, password = password)
        except CreateUser.DoesNotExist:
            return Response({'msg' : "Please Create an account"})

        user_data.update(set__is_login = True)
        return Response({'msg' : "Login Successfully"})

class ShowUserList(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [CustomPermission]
    def get(self, request):
        username = request.headers['username']
        password = request.headers['password']
        if IsAdmin(username, password):
            user_data = CreateUser.objects.all()
            serializer = CreateUserSerializer(user_data, many = True)
            return Response(serializer.data, content_type = 'application/json')
        else:
            user_data = CreateUser.objects.get(username = username, password = password)
            serializer = CreateUserSerializer(user_data)
            return Response(serializer.data, content_type = 'application/json')

    def delete(self, request):
        id = request.data.get('id')
        try:
            user = CreateUser.objects.get(id = id)
        except user.DoesNotExist:
            return Response({'msg' : 'user not exist'})

        user.delete()
        return Response({'msg': 'user deleted successfully'})

class LogoutUser(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [CustomPermissionLogout]
    
    def get(self, request):
        return Response({'msg' : 'Successfully Logout'})
 
