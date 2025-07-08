from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import CustomUser, CustomUserManager
from carts.models import Cart
# Create your views here.
def register_user(request):
    if request.user.is_authenticated:
        return redirect(request.META.get('HTTP_REFERER', '/')) 
    if(request.method == "POST"):
        form = UserRegistrationForm(request.POST) 
        if(form.is_valid()):
            email = form.cleaned_data['email'] 
            password = form.cleaned_data['password1']
            user = CustomUser.objects.create_user(
                email=email,
                password=password
            )
            login(request, user)
            Cart.objects.create(user=user)
            return redirect("home")
    else:
        form = UserRegistrationForm()
    return render(request, "auth/register.html", {'form': form})

def login_user(request):
    if request.user.is_authenticated:
        return redirect(request.META.get('HTTP_REFERER', '/')) 
    if(request.method == "POST"): 
        form = LoginForm(request.POST)
        if(form.is_valid()):
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  
            else:
                messages.error(request, 'Invalid email or password')

    else:
        form = LoginForm()
    return render(request, "auth/login.html", {'form': form}) 
 