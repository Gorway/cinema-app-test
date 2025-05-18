from rest_framework import serializers
from .models import Room, Movie, Screening, Seat, Booking


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["id", "name"]


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "poster_url"]


class ScreeningSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = Screening
        fields = ["id", "movie", "start_time"]


class SeatSerializer(serializers.ModelSerializer):
    is_booked = serializers.SerializerMethodField()

    class Meta:
        model = Seat
        fields = ["id", "row", "number", "is_booked"]

    def get_is_booked(self, seat: Seat) -> bool:
        screening = self.context.get("screening")
        return Booking.objects.filter(screening=screening, seat=seat).exists()
