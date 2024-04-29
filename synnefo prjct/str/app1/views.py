from django.shortcuts import render

from app1.models import *

# Create your views here.

def home(request):
    return render(request,'index.html')

def news1(request):
    return render(request,'news-detail.html')

def stories1(request):
    return render(request,'read-stories.html')

def appoint1(request):
    if request.method=="POST":
        uname=request.POST.get('name')
        uemail=request.POST.get('email')
        s=patient.objects.create(name=uname,email=uemail)
        s.save()
        return render(request,'suceess.html')
