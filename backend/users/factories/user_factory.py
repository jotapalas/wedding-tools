import factory
from factory.faker import Faker
from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username', 'email', )

    username = Faker('user_name')
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    email = Faker('email')
    password = factory.PostGenerationMethodCall('set_password', 'P4$$w0rd')
