from django.contrib.auth.models import User
from booking.models import Booking, STATUS
from .models import OrderBooking

def booking_list(user):
    order_array = OrderBooking.objects.filter(customer=user)
    booking = Booking.objects.filter(customer=user)
    b_array = []
    o_array = []

    for i in booking:
        if i.status == 'Pending':
            b_array.append(str(i.pk))
    
    for i in order_array:
        o_array.append(str(i.booking.pk))

    for i in b_array:
        if i in o_array:
            b_array.remove(i)
    if len(b_array) == 0:
        b_array.append(Booking.objects.first().pk)
    return int(b_array[0])    # first of the booking pk
    


