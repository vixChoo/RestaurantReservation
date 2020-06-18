from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer



class UserRegisterForm(UserCreationForm) :
    email = forms.EmailField()

    class Meta :
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']


class CustomerResegiterForm(forms.ModelForm) :
    class Meta :
        model = Customer
        fields = ['phone_number']