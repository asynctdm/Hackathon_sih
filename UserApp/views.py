from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout 
from .forms import LoginForm
from django.contrib import messages
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModelWithLMHead
from .generalSummarization import llm_init

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from .news_summarization import summarizer


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
def newsSummarization(request):
    if request.method == 'POST':
        userChat = request.POST['userChat']
        response = summarizer(userChat)


        return render(request, 'Hackathon/DashBoard/home.html', {'display': False, 'userChat': userChat, 'machineChat': response})


    return render(request, 'Hackathon/DashBoard/home.html',  {'display': True})

@login_required
def home(request):
    if request.method == 'POST':
        userChat = request.POST['userChat']
        llm = llm_init('/Users/cardinal/testing/vicuna-13b-v1.5-16k.Q2_K.gguf')
        machineChat = llm(userChat)
        print("Machine chat :", machineChat)
        return render(request, 'Hackathon/DashBoard/home.html', {'display': False, 'userChat': userChat, 'machineChat': machineChat})

    return render(request, 'Hackathon/DashBoard/home.html',  {'display': True})

def logout1(request):
    logout(request)
    messages.success(request, 'Successfully Logged out')
    return redirect('/login')