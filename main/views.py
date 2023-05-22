from django.shortcuts import render
from .models import Category,News
# Create your views here.
def Homepage(request):
    categories=Category.objects.all()
    news=News.objects.all()
    context={
        'categories':categories,
        'news':news
    }
    return render(request,'index.html',context)