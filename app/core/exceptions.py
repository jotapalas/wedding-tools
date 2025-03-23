from rest_framework import status


class BaseException(Exception):
    '''
    Custom exception that uses standard HTTP codes.

    Also, detail string is required.
    '''
    default_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self, detail: str | dict, status_code: int = None, *args, **kwargs):
        super().__init__(detail, *args, **kwargs)
        self.detail = detail
        self.status_code = status_code or self.default_code

class ConflictException(BaseException):
    '''
    This exception should be raised to avoid IntegrityError
    '''
    default_code = status.HTTP_409_CONFLICT

class PermissionDeniedException(BaseException):
    '''
    Raised when a user has no access to edit or create one item.
    '''
    default_code = status.HTTP_403_FORBIDDEN


class UnauthorizedException(BaseException):
    '''
    Raised when a given resource that needs authorization is not authenticated.
    '''
    default_code = status.HTTP_401_UNAUTHORIZED

class NotFoundException(BaseException):
    '''
    Raised when a needed resource is not found
    '''
    default_code = status.HTTP_404_NOT_FOUND
