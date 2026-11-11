from django.urls import path,include
from users.views import *
from django.contrib.auth import views as auth_views
app_name = 'user'

urlpatterns = [
    path('/login',login_view,name='login'),
    path('/logout',logout_,name='logout'),
    path('/register',register,name='register'),
    path('/dashboard',dashboard,name='dashboard'),
    ]