from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.

class Blog(models.Model):
  title= models.CharField(max_length=500)
  content= models.TextField()
  subtitle= models.CharField(max_length=500,null=True, blank=True)
  subcontent= models.TextField(null=True, blank=True)
  date= models.DateField(auto_now_add=True)
  img= models.ImageField(upload_to='blog-images/')
  subimg= models.ImageField(upload_to='blog-images/',null=True, blank=True)
  author= models.ForeignKey(User,on_delete=models.CASCADE)
  tags=TaggableManager()

  def __str__(self):
      return self.title
  
  def get_absolute_url(self):
      return reverse("blog_detail", kwargs={"pk": self.pk})
  




