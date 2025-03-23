from .user_admin import CustomUserAdmin
from django.contrib import admin
from django.contrib.auth.models import Group

admin.site.unregister(Group)

__all__ = [
    'CustomUserAdmin',
]
