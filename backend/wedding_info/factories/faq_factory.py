import factory
from wedding_info.models import FAQ


class FAQFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FAQ

    question = factory.Faker("sentence", nb_words=6)
    answer = factory.Faker("text", max_nb_chars=200)
