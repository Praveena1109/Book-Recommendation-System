from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('home/',views.home,name="home"),
    path('loginin/',views.loginin,name="loginin"),
    path('signup/',views.signup,name="signup"),
    path('logout/',views.logoutUser,name="logout"),
    path('favourite/',views.favourite,name="favourite"),
    path('readlist/',views.readlist,name="readList"),
    path('details/<str:pk>/',views.details,name="details"),
    path('popular/',views.popular,name="popular")
]
