from django.shortcuts import redirect, render
from .models import Category,New
from .forms import UploadNews
# Create your views here.
def Homepage(request):
    news=New.objects.select_related('category').all().order_by('-date')
    context={
        'news':news
    }
    return render(request,'index.html',context)


def Detail(request,pk):
    news=New.objects.get(id=pk)
    news.views+=1
    news.save()
    context={
        'new':news
    }
    return render(request,'detail.html',context)


def Upload(request):
    if request.method == 'POST':
        form=UploadNews(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    form=UploadNews()
    
    context={
        'form':form
    }
    return render(request,'upload.html',context)