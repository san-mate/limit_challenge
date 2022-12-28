from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.exceptions import APIException


def exception_handler(exc, context):

    if isinstance(exc, Exception):
        exc = APIException(detail={'error': exc})

    return drf_exception_handler(exc, context)