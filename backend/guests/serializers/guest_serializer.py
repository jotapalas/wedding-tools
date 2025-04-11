from rest_framework import serializers

from guests.models import Guest


class GuestLiteSerializer(serializers.ModelSerializer):
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
            'nickname',
            'email',
            'phone',
            'attending',
            'is_vegan',
            'is_vegetarian',
            'common_allergies',
            'other_allergies',
        )

class GuestSerializer(GuestLiteSerializer):
    same_group_guests = GuestLiteSerializer(many=True, read_only=True)

    class Meta(GuestLiteSerializer.Meta):
        fields = GuestLiteSerializer.Meta.fields + ('same_group_guests',)
