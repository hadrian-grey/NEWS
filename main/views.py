from django.shortcuts import render
from .models import Category
# Create your views here.
def Homepage(request):
    categories=Category.objects.all()
    
    context={
        'categories':categories
    }
    return render(request,'index.html',context)