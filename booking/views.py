from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect , HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from django.contrib.auth.models import User
from .models import Booking, MEAL
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .forms import CreateForm


def home(request) :
    is_home = True
    return render(request,'index.html',{'is_home':is_home, 'title': True})

# Login in is required
class BookingCreateView(LoginRequiredMixin,CreateView):
    form_class = CreateForm

    def form_valid(self, form):
        form.instance.customer = self.request.user
        meal_plan = form.instance.meal_plan
        form.instance.booking_fee = self.change_price(meal_plan)
        return super().form_valid(form)

    def change_price(self, meal_plan):
        if meal_plan == MEAL[0][0]:  
            booking_fee = 100 # breakfast
        elif meal_plan == MEAL[1][0]:
            booking_fee = 200 # lunch  
        elif meal_plan == MEAL[2][0]:
            booking_fee = 300 # dinner
        
        return booking_fee

class BookingDetailView(DetailView) :
    model = Booking

class UserBookingListView(ListView):
        model = Booking
        context_object_name = 'bookings'
        
        def get_queryset(self):
            return Booking.objects.filter(customer=self.request.user).order_by("-date_created")

class BookingUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Booking
    fields = ['meal_plan','reserve_date','reserve_time','people','desc']

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)

    def test_func(self):
        booking = self.get_object()
        if self.request.user == booking.customer :
            return True
        return False