from typing import Any
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.db import transaction


from .models import Room, Screening, Seat, Booking
from .serializers import RoomSerializer, ScreeningSerializer, SeatSerializer


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


class RoomListView(APIView):
    def get(self, request: Any) -> Response:
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)


class ScreeningsByRoomView(APIView):
    def get(self, request: Any, pk: int) -> Response:
        screenings = Screening.objects.filter(room_id=pk).order_by("start_time")
        serializer = ScreeningSerializer(screenings, many=True)
        return Response(serializer.data)


class SeatAvailabilityView(APIView):
    def get(self, request: Any, pk: int) -> Response:
        screening = get_object_or_404(Screening, pk=pk)
        seats = Seat.objects.filter(room=screening.room).order_by("row", "number")
        serializer = SeatSerializer(seats, many=True, context={"screening": screening})
        return Response(serializer.data)


class BookSeatView(APIView):
    def post(self, request: Any) -> Response:
        screening_id = request.data.get("screening_id")
        seat_id = request.data.get("seat_id")

        if not screening_id or not seat_id:
            return Response({"error": "screening_id and seat_id required"}, status=400)

        try:
            with transaction.atomic():
                screening = Screening.objects.select_for_update().get(pk=screening_id)
                seat = Seat.objects.select_for_update().get(pk=seat_id)

                if Booking.objects.filter(screening=screening, seat=seat).exists():
                    return Response({"error": "Seat already booked"}, status=400)

                Booking.objects.create(screening=screening, seat=seat)

                return Response({"success": "Seat booked"}, status=201)

        except Screening.DoesNotExist:
            return Response({"error": "Invalid screening"}, status=404)
        except Seat.DoesNotExist:
            return Response({"error": "Invalid seat"}, status=404)
