from multiprocessing import context
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from app2.models import Major

def my_views(request):
    return render(request,'main.html')

def register(request):
    form= CreateUserForm()
    
    if request.method=='POST':
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been created successfuly.')
            return redirect('log')

    context={'form':form}
    return render(request,'registration/sign_up.html',context)


def log(request):
    if request.method == 'POST':
        u_name = request.POST.get('username')
        p_word=request.POST.get('Password')

        user = authenticate(username= u_name, password=p_word)
        
        if user is not None:
            login(request, user)
            return redirect('search')
        else:
            messages.info(request, 'Username OR password is incorrect')
    
    return render(request,'registration/log.html')


def lm(request):
    return render(request, 'registration/learnmore.html')


