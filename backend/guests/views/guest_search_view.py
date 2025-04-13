from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from guests.serializers import GuestSearchSerializer, GuestSerializer


class GuestSearchView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        serializer = GuestSearchSerializer(data=request.query_params)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        guests = serializer.search()
        if not guests or not guests.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(
            GuestSerializer(guests, many=True).data,
            status=status.HTTP_200_OK,
        )
