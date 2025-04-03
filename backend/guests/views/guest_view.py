from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from guests.models import Guest
from guests.serializers import GuestSerializer


class GuestView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request, guest_id):
        try:
            guest = Guest.objects.get(pk=guest_id)
        except (Guest.DoesNotExist, ValidationError):
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GuestSerializer(guest)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, guest_id):
        try:
            guest = Guest.objects.get(pk=guest_id)
        except (Guest.DoesNotExist, ValidationError):
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GuestSerializer(guest, data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        guest.refresh_from_db()
        
        return Response(
            GuestSerializer(guest).data,
            status=status.HTTP_200_OK,
        )
