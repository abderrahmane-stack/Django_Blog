from django.shortcuts import render , get_object_or_404
from .models import *

# Create your views here.


def home(request):
  blogs = Blog.objects.all().order_by('-id')
  return render(request, 'index.html',{'blogs':blogs})

def blog_detail(request,pk):
  blog=Blog.objects.get(id=pk)
  return render(request, 'detail.html',{'blog':blog})

def get_tags(request,tag_slug):
  blogs = Blog.objects.all().order_by('-id')
  if tag_slug :
    blogs=Blog.objects.get(tags=tag_slug)
    blogs.save()
    return render(request,'index.html',{'blogs':blogs})

def about(request):
  return render(request, 'about.html',{})

def contact(request):
  return render(request, 'contact.html',{})

