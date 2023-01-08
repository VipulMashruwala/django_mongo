from .models import CreateUser
from .serializers import CreateUserSerializer

def IsAdmin(username,password):
    try:
        data = CreateUser.objects.get(username = username, password = password)
    except CreateUser.DoesNotExist:
        return False

    serializer = CreateUserSerializer(data)
    if serializer.data['is_admin'] == True:
        return True
    else:
        return False

def IsLogin(username,password):
    try:
        data = CreateUser.objects.get(username = username, password = password)
    except CreateUser.DoesNotExist:
        return False

    serializer = CreateUserSerializer(data)
    if serializer.data['is_login'] == True:
        return True
    else:
        return False

def IsSameUser(username,password,id):
    user = CreateUser.objects.get(username = username, password = password)
    serializer = CreateUserSerializer(user)
    if id == serializer.data['id']:
        return True
    else:
        return False