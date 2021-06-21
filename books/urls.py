from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage),
    path('home/',views.home),
    path('login/',views.login),
    path('signup/',views.signup),
    path('favourite/',views.favourite),
    path('readlist/',views.readlist),
]
