from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_400_BAD_REQUEST

class MyError(APIException):
    """Readers error class"""
    def __init__(self, msg):
        APIException.__init__(self, msg)
        self.status_code = HTTP_400_BAD_REQUEST
        self.message = msg

class MyError2(APIException):
    """Readers error class"""
    def __init__(self, msg):
        APIException.__init__(self, msg)
        self.status_code = HTTP_400_BAD_REQUEST
        self.message = msg