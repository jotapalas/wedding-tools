from django.urls import path

from guests.views import (
    GuestSearchView,
)


urlpatterns = [
    path(
        'search/',
        GuestSearchView.as_view(),
        name='guests-search',
    ),
]
