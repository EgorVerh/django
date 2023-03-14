from django.http import HttpResponse

from django.shortcuts import render 
from .models import News
from .forms import NewsForm
from django.views  import generic 

# Create your views here.
# def readnews(request):
#     news=News.objects.all()
#     return render(request,'news/readnews.html',{'news':news})

def writenews(request):
    error=''
    if request.method=='POST':
        form=NewsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error="Неверные данные"
    form=NewsForm()
    return render(request,'news/writenews.html',{'form':form,'error':error})


class ChangeNewsView(generic.UpdateView):
   model=News
   template_name='news/writenews.html'
   form_class=NewsForm

class ConcretNewsView(generic.DetailView):
    model=News
    template_name='news/concretnews.html'

class ReadNewsView(generic.ListView):
    model=News
    template_name='news/readnews.html'
