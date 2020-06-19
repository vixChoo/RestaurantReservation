from django.urls import path
from . import views
from .views import (
    home,
    BookingCreateView,
    BookingDetailView,
    UserBookingListView,
    BookingUpdateView
)

urlpatterns = [
    path('',home, name="home"),
    path('booking/new/', BookingCreateView.as_view(template_name='booking_form.html'), name="booking-create"),	
    path('booking/<int:pk>/', BookingDetailView.as_view(template_name='booking_detail.html'), name="booking-detail"),
    path('profile/booking/', UserBookingListView.as_view(template_name='user_booking.html'), name="booking-list"),
    path('profile/booking/<int:pk>/update', BookingUpdateView.as_view(template_name='booking_detail.html'), name="booking-update"),	
]
