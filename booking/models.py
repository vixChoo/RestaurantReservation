from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

STATUS = (
    ('pending', 'Pending'),
    ('confirm', 'Confirm')
)
MEAL = (
    ('breakfast', 'Breakfast'),
    ('lunch', 'Lunch'),
    ('dinner', 'Dinner')
)

# Create your models here.
class Booking(models.Model) :
    reserve_date = models.DateField()
    reserve_time = models.CharField(unique_for_date='reserve_date',max_length=10)
    status = models.CharField(choices=STATUS,default='Pending',max_length=100)
    meal_plan = models.CharField(choices=MEAL,max_length=100)
    people = models.PositiveIntegerField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    desc = models.TextField(blank=True)

    def __str__(self):
        return f'{self.customer.username} {str(self.pk)}'

    def get_absolute_url(self):
        return reverse('booking-detail', kwargs={'pk': self.pk})