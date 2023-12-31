from django.shortcuts import render,redirect
from django.contrib.auth import (
    authenticate, 
    login, 
    logout
)
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from . decorators import check_pin_for
from django.contrib.auth.decorators import login_required
from lock.models import User
# Create your views here.

def login_data(request):
    if request.method == 'POST':
        logout(request)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request,'lock/login.html')

# @login_required
def home(request):
    return render(request,"lock/home.html")

def logout_of_site(request):
    logout(request)
    return redirect('login')

@check_pin_for
def my_phontos(request):
    return render(request,'lock/Gallery.html')

# @login_required
def add_pin(request):
    error = {}
    if request.method == "POST":
        pin_code = request.POST.get('pin')
        try:
            user_pin = User.objects.get(id=request.user.id,pin_password = pin_code)
        except:
            print("you have enter wrong pin")
            user_pin = None
        if user_pin is not None:
            request.session['session_id_data'] = request.user.id
            return redirect('my_phontos')
    context = {}
    return render(request,'lock/security.html',context)


def remove_session(request):
    try:
        del request.session['session_id_data']
    except  KeyError:
        pass
    return redirect("home")

from django.http import HttpResponseRedirect,HttpResponse,HttpRequest

def about(request):

    return HttpResponse("about page")