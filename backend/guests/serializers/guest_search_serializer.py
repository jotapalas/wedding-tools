from rest_framework import serializers
from guests.models import Guest


class GuestSearchSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    nickname = serializers.CharField(required=False)

    class Meta:
        fields = (
            'first_name',
            'last_name',
            'nickname',
        )
    
    def validate(self, data):
        if not data:
            raise serializers.ValidationError('No search data provided')
        
        return super().validate(data)

    def search(self):
        filters = {
            f'{key}__icontains': value for key, value in self.validated_data.items()
        }
        
        return Guest.objects.filter(**filters)
            