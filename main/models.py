from typing import Any
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    
class News(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='news/')
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    news=RichTextField()
    headline=models.BooleanField(default=False)
    breaking=models.BooleanField(default=False)
    author=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title