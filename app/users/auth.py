from django.contrib.auth.backends import BaseBackend
from users.models import User


class EmailAuthBackend(BaseBackend):
    """
    Custom authentication backend.

    Allows users to log in using their email address.
    """

    def authenticate(self, request, username=None, password=None):
        """
        Overrides the authenticate method to allow users to log in using their email address.
        """
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
