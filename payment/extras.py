from django.contrib.auth.models import User
from booking.models import Booking, STATUS
from .models import OrderBooking

def booking_list(user):
    booking = Booking.objects.filter(customer=user)
    b_array = []

    for i in booking:
        if i.status == 'Pending':
            b_array.append(str(i.pk))
    
    if len(b_array) == 0:
        b_array.append(booking.first().pk)
    return int(b_array[-1])    # last of the booking pk
    


