from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect , HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import braintree, os, stripe
from django.conf import settings

stripe.api_key = "sk_test_51GvhRuJF8iLkitsptTP8k3FSUpQrHdiBHDEuQ3wNuOMsf0tmGDKbugfd6gG2W0VS30KfebITPrgtrzU8K1BDvdDl00Cu8dnxcZ"

@login_required
def checkout(request):
    if request.method == 'POST':
        user = request.user

        customer = stripe.Customer.create(
            email = user.email,
            name = user.first_name + user.last_name,
            phone = user.customer.phone_number,
            description="My First Test Customer (created for API docs)",
            source = request.POST['stripeToken']
            
        )
        charge = stripe.Charge.create(
            customer=customer,
            amount=2000,
            currency="myr",
            description="My 10PM testing)",
        )
        messages.success(request, f'PAYMENT SUCCESSFUL')

    return render(request,'checkout.html')


