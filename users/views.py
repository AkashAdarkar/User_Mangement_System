from django.shortcuts import render
from django.http import HttpResponse

def register(request): #forget the "request" argument here.....
  #changed return HttpResponse("register") to this ...
  return render(request,'users/register.html')


def login(request):
    return render(request,'users/login.html')

def homePage(request):
    return render(request,'users/index.html')

def aboutPage(request):
    return render(request,'users/about.html')