from django.core.management.base import BaseCommand
from datetime import date
from members.models import Booking

class Command(BaseCommand):
    help = 'Mark expired bookings'

    def handle(self, *args, **kwargs):
        today = date.today()

        expired = Booking.objects.filter(
            booking_date__lt=today,
            is_expired=False
        )

        count = expired.update(is_expired=True)

        if count == 0:
            self.stdout.write("No expired bookings found")
        else:
            self.stdout.write(self.style.SUCCESS(f"{count} bookings marked as expired"))