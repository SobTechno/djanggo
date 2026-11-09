from django.shortcuts import render,redirect
from django.contrib.auth import logout
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def register(request):
    return render(request,'auth/login')


def login_(request):
    if request.method == 'GET':
        form = LoginForm()
        content = {'form':form}
        return render(request,'auth/login.html',content)
    else:
        form = LoginForm(request.POST)
        if form.is_valid:
            username= request.POST['username']
            password= request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/accounts/dashboard')
            else:
                return redirect('/')

@login_required
def dashboard(request):
    return HttpResponse(request,'hooooy')

@login_required
def logout_(request):
    user = request
    if request.user.is_authenticated:
        logout(user)
        return redirect('/')
    else:
        return redirect('/')
      

