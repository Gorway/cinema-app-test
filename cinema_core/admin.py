from django.contrib import admin
from .models import Room, Movie, Screening, Seat, Booking


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title",)


@admin.register(Screening)
class ScreeningAdmin(admin.ModelAdmin):
    list_display = ("id", "movie", "room", "start_time")
    list_filter = ("room", "start_time")
    search_fields = ("movie__title", "room__name")


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ("id", "room", "row", "number")
    list_filter = ("room", "row")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "screening", "seat", "created_at")
    list_filter = ("screening", "created_at")
