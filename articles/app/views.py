from django.shortcuts import render
from .models import Article
# Create your views here.
def index(request):
    data=Article.objects.all().order_by('id')
    context={
        'data':data
    }
    return render(request,'index.html',context)

def details(request,pk):
    data1 = Article.objects.get(id=pk)
    context = {
        'data1':data1
    }
    return render(request,'details.html',context)