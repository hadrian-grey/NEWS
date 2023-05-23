from django.shortcuts import render
from .models import Category,News
# Create your views here.
def Homepage(request):
    news=News.objects.select_related('category').all()
    context={
        'news':news
    }
    return render(request,'index.html',context)


def Upload(request):
    return render(request,'upload.html')