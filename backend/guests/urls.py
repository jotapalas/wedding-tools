from django.urls import path

from guests.views import (
    GuestSearchView,
    GuestView,
)


urlpatterns = [
    path(
        'search/',
        GuestSearchView.as_view(),
        name='guests-search',
    ),
    path(
        'guest/<str:guest_id>/',
        GuestView.as_view(),
        name='guests-detail',
    ),
]
