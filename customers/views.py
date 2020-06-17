from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect , HttpResponse
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request) :
    return HttpResponse('<h1>Blog Home</h1>')

def register(request) :
    if request.method == 'POST' :
        form = UserRegisterForm(request.POST)
        if form.is_valid() :
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}, You can log in now!')
            return redirect('login')
    else :
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
    
@login_required
def profile(request) :
    return render(request,'profile.html')