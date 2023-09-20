from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout 
from .forms import LoginForm
from django.contrib import messages

# Create your views here.
def Login(request):
    if request.method == 'POST':
        id = request.POST['userid']
        password = request.POST['password']
        user = authenticate(username=id, password=password)
        print('user', user)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, 'Invalid Username or Password')
            
    return render(request, 'Hackathon/AuthModule/Authentication/login.html')

@login_required
def index(request):
    return render(request, 'Hackathon/DashBoard/home.html')

def logout1(request):
    logout(request)
    messages.success(request, 'Successfully Logged out')
    return redirect('/login')