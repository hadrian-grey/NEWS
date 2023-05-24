from typing import Any
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    
class New(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='news/')
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    news=RichTextField()
    headline=models.BooleanField(default=False,help_text='Choose if the news should be lsited among the main headlines')
    trending=models.BooleanField(default=False,help_text='Choose if the news should be lsited among the trending news')
    breaking=models.BooleanField(default=False,help_text='Choose if the news should be lsited among the breaking news')
    date=models.DateTimeField(auto_now_add=True)
    author=models.CharField(max_length=200)
    views=models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.title
    
class Advert(models.Model):
    image=models.ImageField(upload_to='advert/',blank=True,null=True)
    content=models.TextField(blank=True,null=True)
    name=models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.name


class Comment(models.Model):
    news=models.ForeignKey(New,on_delete=models.CASCADE,related_name='comments')
    comment=models.TextField()
    name=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name    
    
class Media(models.Model):
    youtube_url=models.URLField()
    date=models.DateTimeField(auto_now_add=True)
    video_file=models.FileField(upload_to='video/',blank=True,null=True)
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    

    
    