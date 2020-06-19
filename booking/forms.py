from django import forms
from .models import Booking
import datetime
from django.core.exceptions import ValidationError
from django.conf import settings
from django.core.validators import RegexValidator

class CreateForm(forms.ModelForm) :
    reserve_time = forms.RegexField(label="Time", 

                            regex = "((1[0-2]|0?[1-9]):([0-5][0-9])?([AaPp][Mm]))",
                            error_messages = {"invalid" : "Please Provide Time in HH:MM(am/pm) format!",
                                              "unique_for_date" : "Reserve time has been booked. Please Choose Another Time"},
                            widget= forms.TextInput
                           (attrs={'id':'book_time'}))

    reserve_date = forms.DateField(label="Date",
                            widget= forms.TextInput
                           (attrs={'id':'book_date'}),
                         input_formats=settings.DATE_INPUT_FORMATS)
    people = forms.IntegerField(label="Number of perople",min_value=1,max_value=50,help_text='Maximum 50 people')
    desc = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'ie. Celebration' }),label="Description",required=False)

    class Meta :
        model = Booking
        fields = ['meal_plan','reserve_date','reserve_time', 'people','desc']


        