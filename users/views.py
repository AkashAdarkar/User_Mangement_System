from django.shortcuts import render
from django.http import HttpResponse

def register(request): #forget the "request" argument here.....
    return HttpResponse("Register")    


def login(request):
    return HttpResponse("Login")

def homePage(request):
    return HttpResponse("Home")

def aboutPage(request):
    return HttpResponse("About")