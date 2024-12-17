from django.shortcuts import render
from .models import Article
from django.db.models import Q
# Create your views here.


def index(request):
    data=Article.objects.all()
    # print(data)
    if request.method=="POST":
        search=request.POST.get("search")
        data=Article.objects.filter(Q(name__icontains=search) | Q( description__icontains=search))
    context={
        'data':data
    }
    return render(request,'index.html',context)

def details(request,prk):
    data1=Article.objects.get(id=prk)
    context={
        'data1':data1
    }
    return render(request,'details.html',context)