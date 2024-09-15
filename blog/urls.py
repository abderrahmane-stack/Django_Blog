from django.urls import path ,include 
from .views import *
urlpatterns = [
  path('',home,name='index'),
  path('blog_detail/<int:pk>',blog_detail,name='blog_detail'),
  path('about',about,name='about'),
  path('contact',contact,name='contact'),
] 
