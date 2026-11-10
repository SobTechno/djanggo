from django.shortcuts import render,redirect
from django.contrib.auth import logout
from .forms import LoginForm,RegisterForm
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        content = {'form':form}
        return render(request,'auth/register.html',content)
    else:
        form = RegisterForm(request.POST)
        if form.is_valid:
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 == password2 :
                user = User.objects.filter(username=username).first()
                if user:
                    return redirect('user:register')
                else:
                    user = User.objects.create_user(username=username,password=password1)
                    login(request,user)
                    return redirect('user:dashboard')
            else:
                return redirect('user:register')



def login_view(request):
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
      

