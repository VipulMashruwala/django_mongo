from rest_framework.permissions import BasePermission
from .models import Users, Subject, CreateUser
from .serializers import CreateUserSerializer
from rest_framework.response import Response
from .utils import IsAdmin, IsLogin, IsSameUser

class CustomPermissionUser(BasePermission):
    def has_permission(self, request, view):
        username = request.headers['username']
        password = request.headers['password'] 
        
        if request.method == 'GET':
            if IsLogin(username, password):
                return True
            else:
                return False

        if request.method == 'POST':
            if IsLogin(username, password):
                id = request.data['id']
                return IsSameUser(username, password, id)
            else:
                return False

        if request.method == 'PUT':
            if IsLogin(username, password):
                id = request.data['id']
                return IsSameUser(username, password, id)
            else:
                return False

        if request.method == 'DELETE':
            if IsLogin(username, password):
                id = request.data['id']
                return IsSameUser(username, password, id)
            else:
                return False

class CustomPermission(BasePermission):
    def has_permission(self, request, view):        
        username = request.headers['username']
        password = request.headers['password']
        if request.method == 'GET':
            if IsLogin(username,password):
                return True
            else:
                return False   

        if request.method == 'DELETE':
            if IsLogin(username, password):
                return IsAdmin(username, password)
            else:
                return False          

class CustomPermissionSubject(BasePermission):
    def has_permission(self, request, view):
        username = request.headers['username']
        password = request.headers['password']
        if request.method == 'GET':
            if IsLogin(username,password):
                return True
            else:
                return False

        if request.method == 'POST':
            if IsLogin(username, password):
                return IsAdmin(username,password)
            else:
                return False
        
class CustomPermissionLogout(BasePermission):
    def has_permission(self, request, view):
        username = request.headers['username']
        password = request.headers['password']
        if request.method == 'GET':
            if IsLogin(username, password):
                user_data = CreateUser.objects(username = username, password = password)
                user_data.update(set__is_login = False)
                return True
            else:
                return False