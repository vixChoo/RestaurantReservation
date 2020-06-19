from django.db import models
from booking.models import Booking, STATUS

class Payment(models.Model): 
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS,default=STATUS[0][1],max_length=100)


