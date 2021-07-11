from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm
from django.contrib import messages
from .models import *

# Create your views here.

def home(request):
    books = Book.objects.all().order_by('AvgBookRating')
    return render(request,'books/home.html',{'books': books})

def homepage(request):
    return render(request,'books/homepage.html')

def login(request):
    context = {}
    return render(request,'books/login.html', context)

def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Now Log In.')
            form.save()
            return redirect('login')
    else:
        form = CreateUserForm()
    context = {'form': form}
    return render(request,'books/signup.html', context)

def favourite(request):
    return render(request,'books/favourite.html')

def readlist(request):
    return render(request,'books/readlist.html')

def details(request, pk):
    book = Book.objects.get(id=pk)
    return render(request,'books/details.html',{'book': book})

def foryou(request):
    return render(request,'books/foryou.html')

def popular(request):
    books = Book.objects.all()
    return render(request,'books/popular.html',{'books':books})
