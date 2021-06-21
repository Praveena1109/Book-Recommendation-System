from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
        return render(request,'books/home.html')

def homepage(request):
    return render(request,'books/homepage.html')

def login(request):
    return render(request,'books/login.html')

def signup(request):
    return render(request,'books/signup.html')

def favourite(request):
    return render(request,'books/favourite.html')

def readlist(request):
    return render(request,'books/readlist.html')
