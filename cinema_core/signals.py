from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Room, Seat


@receiver(post_save, sender=Room)
def create_seats_for_room(
    sender, instance: Room, created: bool, **kwargs: object
) -> None:
    if created:
        seats = [
            Seat(room=instance, row=row, number=number)
            for row in range(1, 11)
            for number in range(1, 9)
        ]
        Seat.objects.bulk_create(seats)
