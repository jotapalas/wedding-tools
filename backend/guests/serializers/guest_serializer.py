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
            'email',
            'phone',
            'attending',
            'special_diet',
            'allergies',
            'pre_wedding',
        )

class GuestSerializer(GuestLiteSerializer):
    same_group_guests = serializers.SerializerMethodField(read_only=True)

    class Meta(GuestLiteSerializer.Meta):
        fields = GuestLiteSerializer.Meta.fields + ('same_group_guests',)

    def get_same_group_guests(self, obj):
        # Get the list of guests in the same group as the current guest
        same_group_guests = obj.same_group_guests
        if same_group_guests:
            same_group_guests = same_group_guests.filter(
            attending=Guest.AttendingStatusChoices.DIDNT_RESPOND
        )
        return GuestLiteSerializer(same_group_guests, many=True).data
