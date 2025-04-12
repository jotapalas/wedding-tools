from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from wedding_info.models import FAQ
from wedding_info.serializers import FAQSerializer


class GuestView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        faqs = FAQ.objects.all()
        serializer = FAQSerializer(faqs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)