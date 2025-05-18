from django.urls import path
from .views import (
    RoomListView,
    ScreeningsByRoomView,
    SeatAvailabilityView,
    BookSeatView,
    index,
)

urlpatterns = [
    path("", index),
    path("rooms/", RoomListView.as_view()),
    path("rooms/<int:pk>/screenings/", ScreeningsByRoomView.as_view()),
    path("screenings/<int:pk>/seats/", SeatAvailabilityView.as_view()),
    path("book/", BookSeatView.as_view()),
]
