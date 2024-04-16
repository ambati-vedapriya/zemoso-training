from datetime import datetime
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
from rest_framework import status


class UserNotFoundException(APIException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    response.data["timeStamp"] = str(datetime.utcnow())
    response.status_code = status.HTTP_404_NOT_FOUND

    return response
