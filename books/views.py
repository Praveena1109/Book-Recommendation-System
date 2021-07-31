from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from django.db.models import Count,Q
from .models import *

# Create your views here.

@login_required(login_url='loginin')
def home(request):
    books = Book.objects.all().order_by('BookTitle')
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
def search(request):
    query = request.GET['query']
    booksTitle = Book.objects.filter(BookTitle__icontains=query)
    booksAuthor = Book.objects.filter(BookAuthor__icontains=query)
    books = booksTitle.union(booksAuthor)
    return render(request,'books/search.html',{'books': books})

@login_required(login_url='loginin')
def favourite_add(request, id):
    book = get_object_or_404(Book, id=id)
    if book.favourites.filter(id=request.user.id).exists():
        book.favourites.remove(request.user)
    else:
        book.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required(login_url='loginin')
def favourite(request):
    favourites = Book.objects.filter(favourites = request.user)
    return render(request,'books/favourite.html',{'favourites': favourites})

@login_required(login_url='loginin')
def readlist_add(request, id):
    book = get_object_or_404(Book, id=id)
    if book.readlist.filter(id=request.user.id).exists():
        book.readlist.remove(request.user)
    else:
        book.readlist.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required(login_url='loginin')
def readlist(request):
    readlist = Book.objects.filter(readlist = request.user)
    return render(request,'books/readlist.html',{'readlist':readlist})

@login_required(login_url='loginin')
def category(request):
    books = Book.objects.all()
    categories = Book.objects.values("Genre").annotate(count=Count('Genre')).filter(count__gt=1).order_by("-count")
    return render(request,'books/category.html', {'categories':categories, 'books':books})

@login_required(login_url='loginin')
def details(request, pk):
    book = Book.objects.get(id=pk)
    return render(request,'books/details.html',{'book': book})

def recommend(BookTitle):
    book_details = pd.read_csv('book_details.csv')
    user_rating_pivot = books_details.pivot(index = 'BookTitle', columns = 'UserID', values = 'BookRating').fillna(0)
    user_rating_matrix = csr_matrix(user_rating_pivot.values)
    model_knn = NearestNeighbors(metric = 'cosine', algorithm = 'brute')
    model_knn.fit(user_rating_matrix)
    query_index = np.where(user_rating_pivot.index == BookTitle)[0][0]
    distances, indices = model_knn.kneighbors(user_rating_pivot.iloc[query_index,:].values.reshape(1, -1), n_neighbors = 4)
    recommend_list= []
    for i in indices[0]:
        recommend_list.append(user_rating_pivot.index[i])

@login_required(login_url='loginin')
def foryou(request):
    return render(request,'books/foryou.html')

@login_required(login_url='loginin')
def popular(request):
    books = Book.objects.all()
    return render(request,'books/popular.html',{'books':books})
