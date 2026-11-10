from django.urls import path
from users.views import *
app_name = 'user'

urlpatterns = [
    path('/login',login_view,name='login'),
    path('/logout',logout_,name='logout'),
    path('/register',register,name='register'),
    path('/dashboard',dashboard,name='dashboard')
    ]