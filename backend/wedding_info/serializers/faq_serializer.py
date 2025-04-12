from rest_framework import serializers

from wedding_info.models import FAQ


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = (
            'question',
            'answer',
        )
  