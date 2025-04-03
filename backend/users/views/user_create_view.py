from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from core.exceptions import BaseException
from users.serializers.input import UserCreateSerializer


class UserCreateView(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        except BaseException as err:
            return Response(
                err.detail,
                status=err.status_code
            )
