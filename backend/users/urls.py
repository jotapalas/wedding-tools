from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import (
    UserCreateView,
)


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='users-login'),
    path('refresh/', TokenRefreshView.as_view(), name='users-refresh-token'),  
    path('create/', UserCreateView.as_view(), name='users-create'),
]
