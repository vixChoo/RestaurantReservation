from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect , HttpResponse
from .forms import UserRegisterForm, CustomerResegiterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from .models import Customer

def home(request) :
    return HttpResponse('<h1>Blog Home</h1>')

def register(request) :
    if request.method == 'POST' :
        u_form = UserRegisterForm(request.POST)
        c_form = CustomerResegiterForm(request.POST)
        if u_form.is_valid() or c_form.is_valid():
            new_user = u_form.save()
            c_form.instance.customer = new_user
            c_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}, You can log in now!')
            return redirect('login')
        
    else :
        u_form = UserRegisterForm()
        c_form = CustomerResegiterForm()
        return render(request, 'register.html', {'uform': u_form, 'cform' : c_form})

@login_required
def profile(request) :
    return render(request,'profile.html')