from django.db import models
from booking.models import Booking
from django.contrib.auth.models import User

# Create your models here.
class OrderBooking(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.booking.pk}'

