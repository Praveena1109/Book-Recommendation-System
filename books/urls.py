from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('home/',views.home,name="home"),
    path('loginin/',views.loginin,name="loginin"),
    path('signup/',views.signup,name="signup"),
    path('logout/',views.logoutUser,name="logout"),
    path('search/',views.search, name="search"),
    path('fav/<int:id>/',views.favourite_add,name="favourite_add"),
    path('favourite/',views.favourite,name="favourite"),
    path('readlist/<int:id>/',views.readlist_add,name="readlist_add"),
    path('readlist/',views.readlist,name="readlist"),
    path('category/',views.category,name="category"),
    path('details/<str:pk>/',views.details,name="details"),
    path('popular/',views.popular,name="popular"),
    path('foryou/',views.foryou,name="foryou")
]
