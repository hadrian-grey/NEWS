from django.shortcuts import redirect, render
from .models import New,Comment,Media
# Create your views here.
def Homepage(request):
    news=New.objects.select_related('category').all().order_by('-date')
    media=Media.objects.select_related('category').all().order_by('-date')[:4]
    context={
        'news':news,
        'media':media
    }
    return render(request,'index.html',context)


def Detail(request,pk):
    news=New.objects.get(id=pk)
    if request.POST:
        name=request.POST.get('name')
        email=request.POST.get('email')
        comment=request.POST.get('comment')
        
        new_comment=Comment.objects.create(comment=comment,name=name,email=email,news=news)
        new_comment.save()
        return redirect('detail',pk=pk)
    news.views+=1
    news.save()
    context={
        'new':news
    }
    return render(request,'detail.html',context)

def privacy(request):
    return render(request,'privacy.html')

