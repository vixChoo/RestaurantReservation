from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect , HttpResponse
from .forms import UserRegisterForm, CustomerResegiterForm, CustomerUpdateForm,UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request) :
    return HttpResponse('<h1>Blog Home</h1>')

def register(request) :
    if request.method == 'POST' :
        u_form = UserRegisterForm(request.POST)
        c_form = CustomerResegiterForm(request.POST)
        if u_form.is_valid():
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
    if request.method == 'POST' :
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = CustomerUpdateForm(request.POST, request.FILES,instance=request.user.customer)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
        
    else :
        user_form = UserUpdateForm(instance=request.user)
        profile_form = CustomerUpdateForm(instance=request.user.customer)
        return render(request,'profile.html', {'uform' : user_form, 'pform' : profile_form})



    