from django.urls import path, reverse_lazy
from .views import  register_user, logout_user, login_user
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", login_user, name="login"),
    path("register/", register_user, name="register"),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
]
