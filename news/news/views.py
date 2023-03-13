from django.http import HttpResponse

from django.shortcuts import render 
from .models import News
from .forms import NewsForm

# Create your views here.
def readnews(request):
    news=News.objects.all()
    return render(request,'news/readnews.html',{'news':news})

def writenews(request):
    error=''
    if request.method=='POST':
        form=NewsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error="неверные данные"
    form=NewsForm()
    return render(request,'news/writenews.html',{'form':form,'error':error})

def write(request):
    return HttpResponse('All done')

