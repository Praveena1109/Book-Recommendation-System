from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('home/',views.home,name="home"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('favourite/',views.favourite,name="favourite"),
    path('readlist/',views.readlist,name="readList"),
    path('details/<str:pk>/',views.details,name="details")
]
