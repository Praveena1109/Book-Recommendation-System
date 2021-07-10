from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    books = Book.objects.all()
    return render(request,'books/home.html',{'books': books})

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

def details(request, pk):
    book = Book.objects.get(id=pk)
    return render(request,'books/details.html',{'book': book})
