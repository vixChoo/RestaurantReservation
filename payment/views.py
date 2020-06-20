from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from booking.models import Booking, STATUS
from .models import OrderBooking
from .extras import booking_list

import braintree, os, stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_PRIVATE_KEY


@login_required()
def add_order(request, **kwargs):
    user = request.user
    # filter bookings by id
    booking = Booking.objects.filter(id=kwargs.get('booking_id')).first()
    # create OrderBooking of the selected booking
    order, created = OrderBooking.objects.get_or_create(booking=booking,customer=user)
    return redirect('/payment/checkout/', order.id)


@login_required
def checkout(request):
    user = request.user
    booking_id = booking_list(user)
    booking = Booking.objects.filter(id=booking_id).first()
    stripe_key = settings.STRIPE_PUBLIC_KEY
    if booking.status == 'Pending': 
        if request.method == 'POST':
            amount = booking.booking_fee
            customer = stripe.Customer.create(
                email = user.email,
                name = user.first_name + user.last_name,
                phone = user.customer.phone_number,
                description= f'Username : {user.username}',
                source = request.POST['stripeToken']
                
            )
            charge = stripe.Charge.create(
                customer=customer,
                amount=(amount*100),
                currency="myr",
                description=f'Payment For Booking Id : {booking.id}',
            )
            messages.success(request, f'PAYMENT SUCCESSFUL')
            booking.status = 'Confirm' # CONFIRM
            booking.save()

            return redirect('booking-detail' ,pk=booking.id)
    else:
        messages.warning(request, f'Payment Already Made!')
        return redirect(reverse('booking-detail', args=[booking.id]))

    return render(request,'checkout.html', {'booking':booking,'stripe_key':stripe_key})


