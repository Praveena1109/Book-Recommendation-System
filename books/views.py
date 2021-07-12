from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.

@login_required(login_url='loginin')
def home(request):
    books = Book.objects.all().order_by('AvgBookRating')
    return render(request,'books/home.html',{'books': books})

def homepage(request):
    return render(request,'books/homepage.html')

def loginin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is Incorrect')
        context = {}
        return render(request,'books/loginin.html', context)

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}! Now Log In.')
                form.save()
                return redirect('loginin')
        else:
            form = CreateUserForm()
        context = {'form': form}
        return render(request,'books/signup.html', context)

def logoutUser(request):
    logout(request)
    return redirect('homepage')

@login_required(login_url='loginin')
def favourite(request):
    return render(request,'books/favourite.html')

@login_required(login_url='loginin')
def readlist(request):
    return render(request,'books/readlist.html')

@login_required(login_url='loginin')
def details(request, pk):
    book = Book.objects.get(id=pk)
    return render(request,'books/details.html',{'book': book})

@login_required(login_url='loginin')
def foryou(request):
    return render(request,'books/foryou.html')

@login_required(login_url='loginin')
def popular(request):
    books = Book.objects.all()
    return render(request,'books/popular.html',{'books':books})
