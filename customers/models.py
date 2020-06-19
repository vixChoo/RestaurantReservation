from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model) :
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=100)

    # Shows in admin site
    def __str__(self):
        return f'{self.customer.username} Profile'