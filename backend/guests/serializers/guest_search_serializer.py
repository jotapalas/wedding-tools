from rest_framework import serializers
from guests.models import Guest

from django.db.models import Q


class GuestSearchSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    class Meta:
        fields = (
            'first_name',
            'last_name',
        )
    
    def validate(self, data):
        if not data:
            raise serializers.ValidationError('No search data provided')
        
        return super().validate(data)

    def search(self):
        first_name_query = Q()
        last_name_query = Q()

        first_name = self.validated_data.get('first_name')
        if first_name:
            first_name_query = (
                Q(first_name__icontains=first_name)
                | Q(nickname__icontains=first_name)
            )
        
        last_name = self.validated_data.get('last_name')
        if last_name:
            last_name_query = Q(last_name__icontains=last_name)
        
        return Guest.objects.filter(first_name_query & last_name_query)
            