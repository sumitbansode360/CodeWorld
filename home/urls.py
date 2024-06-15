from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('signup/',views.signUphandle,name="signUphandle"),
    path('login/',views.logInhandle,name="logInhandle"),    
    path('logout/',views.logOuthandle,name="logOuthandle"), # name and views."name" must be same 
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('create/', views.create, name='create'),
]
