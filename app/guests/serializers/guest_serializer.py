from rest_framework import serializers

from guests.models import Guest


class GuestSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    attending = serializers.ChoiceField(
        choices=[
            Guest.AttendingStatusChoices.YES,
            Guest.AttendingStatusChoices.NO,
        ],
        required=True,
    )

    class Meta:
        model = Guest
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'attending',
            'is_vegan',
            'is_vegetarian',
            'common_allergies',
            'other_allergies',
        )
