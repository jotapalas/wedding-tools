from rest_framework import serializers

from wedding_info.models import FAQ


class FAQSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = FAQ
        fields = (
            'id',
            'question',
            'answer',
            'include_moodboard',
            'include_accommodation',
        )
  