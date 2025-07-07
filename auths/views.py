from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.

def register_user(request):
    if(request.method == "POST"):
        form = UserRegistrationForm(request.POST) 
        if(form.is_valid()):
            username = form.cleaned_data['username'] 
            password = form.cleaned_data['password1']
            user = User.objects.create_user(
                username=username,
                password=password
            )
            login(request, user)
    else:
        form = UserRegistrationForm()
    return render(request, "auth/register.html", {'form': form})

def login_user(request):
    if(request.method == "POST"):
        form = LoginForm(request.POST)
        if(form.is_valid()):
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('register')  # Replace with your desired redirect
            else:
                messages.error(request, 'Invalid username or password')

    else:
        form = LoginForm()
    return render(request, "auth/login.html", {'form': form}) 

def logout_user(request):

    return