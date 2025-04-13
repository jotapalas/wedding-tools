from django.urls import path

from wedding_info.views import (
    FAQView,
)


urlpatterns = [
    path(
        'faqs/',
        FAQView.as_view(),
        name='wedding-info-faqs',
    ),
]
