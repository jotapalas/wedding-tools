import factory
from guests.models import Guest, GuestGroup


class GuestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Guest

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

class GuestGroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GuestGroup
