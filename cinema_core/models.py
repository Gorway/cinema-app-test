from django.db import models


class Room(models.Model):
    name: str = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    title: str = models.CharField(max_length=200)
    poster_url: str = models.URLField()

    def __str__(self) -> str:
        return self.title


class Screening(models.Model):
    room: models.ForeignKey[Room] = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name="screenings"
    )
    movie: models.ForeignKey[Movie] = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="screenings"
    )
    start_time: models.DateTimeField = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.movie.title} at {self.start_time.strftime('%H:%M')} in {self.room.name}"


class Seat(models.Model):
    room: models.ForeignKey[Room] = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name="seats"
    )
    row: int = models.PositiveIntegerField()
    number: int = models.PositiveIntegerField()

    class Meta:
        unique_together = ("room", "row", "number")
        ordering = ["row", "number"]

    def __str__(self) -> str:
        return f"Row {self.row} Seat {self.number} ({self.room.name})"


class Booking(models.Model):
    screening: models.ForeignKey[Screening] = models.ForeignKey(
        Screening, on_delete=models.CASCADE, related_name="bookings"
    )
    seat: models.ForeignKey[Seat] = models.ForeignKey(
        Seat, on_delete=models.CASCADE, related_name="bookings"
    )
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("screening", "seat")

    def __str__(self) -> str:
        return f"Booking: {self.seat} for {self.screening}"
