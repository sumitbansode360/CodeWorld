from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.blog, name='home'),
    path('search/',views.search,name="search"),   # keep search urls first order of urls matters
    path('postComment/',views.postComment,name="postComment"),
    path('<str:slug>/', views.blogpost, name='blogPost'),
    
]

#  if django travles from top to bottom and if django gets results for an url then it will not proceed further therfore other urls will not excute