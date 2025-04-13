from django.db.models import Q
from rest_framework import serializers
from users.models import User
from core.exceptions import ConflictException


class UserCreateSerializer(serializers.Serializer):
    """
    Serializer for creating or updating users
    """
    username = serializers.CharField(
        max_length=150,
        required=True
    )
    first_name = serializers.CharField(
        max_length=150,
        required=False
    )
    last_name = serializers.CharField(
        max_length=150,
        required=False
    )
    email = serializers.EmailField(
        required=True,
    )
    password = serializers.CharField(
        max_length=128,
        required=True,
        write_only=True
    )

    def create(self, validated_data):
        email = validated_data['email']
        username = validated_data['username']
        existing_user = User.objects.filter(
            Q(username=username)
            | Q(email=email)
        ).first()

        if existing_user:
            conflict_field = 'username' if existing_user.username == username else 'email'
            message = f'User with that {conflict_field} already exists.'
            raise ConflictException({
                conflict_field: message
            })
        
        return User.objects.create_user(**validated_data)
