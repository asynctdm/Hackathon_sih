from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout 
from .forms import LoginForm
from django.contrib import messages

from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModelWithLMHead

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))


from langchain.llms.huggingface_pipeline import HuggingFacePipeline
import faulthandler

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
    if request.method == 'POST':
        userChat = request.POST['userChat']
        faulthandler.enable()
        def model(model_id: str, task: str, model_kwargs: dict, pipeline_kwargs: dict):
            embedding_func = HuggingFacePipeline.from_model_id(
            model_id='mrm8488/t5-base-finetuned-summarize-news',
            task='summarization',
            model_kwargs=model_kwargs,
            pipeline_kwargs=pipeline_kwargs,
            )
            return embedding_func
        model_name = 'mrm8488/t5-base-finetuned-summarize-news',
        model_kwargs = {'temperature': 0.75, 'top_k': 10, 'top_p': 0.5, 'max_length': 150, 'min_length': 10,'num_beams': 2, 'num_return_sequences': 2, 'repetition_penalty': 2.5, 'length_penalty': 1.0}
        pipeline_kwargs = {'repetition_penalty': 2.5, 'length_penalty': 1.0}

        model = model(model_name,'summarization', model_kwargs, pipeline_kwargs)
        edited_prompt = f'Summarise this news article\n{userChat}'
        response = model._call(prompt=edited_prompt)


        return render(request, 'Hackathon/DashBoard/home.html', {'display': False, 'userChat': userChat, 'machineChat': response})


    return render(request, 'Hackathon/DashBoard/home.html',  {'display': True})

def logout1(request):
    logout(request)
    messages.success(request, 'Successfully Logged out')
    return redirect('/login')