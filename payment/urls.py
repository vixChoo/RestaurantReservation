from django.urls import path
from . import views
from .views import (
    checkout,
    add_order
)


urlpatterns = [
    path('checkout/', checkout, name="checkout"),	
    path('add-order/<int:booking_id>', add_order, name="add_order"),	

]