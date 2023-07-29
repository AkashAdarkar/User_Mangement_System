from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from .forms import UserForm


def register(request): #forget the "request" argument here.....
  form = UserForm()
  if request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')

  context = {'form':form}
  return render(request,'users/register.html',{'context':context})

def updateUser(request,pk):
    user =User.objects.get(id=pk)
    form = UserForm(instance=user)
    if request.method == 'POST':
        form =UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('/')


    context={'form':form}
    return render(request,'users/update_user.html',{'context':context})

def deleteUser(request,pk):
    user=User.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('/')

    context={'user':user}
    return render(request,'users/delete_user.html',{'context':context})

def login(request):
    return render(request,'users/login.html')

def homePage(request):
    user = User.objects.all()
    context={'user':user}
    return render(request,'users/index.html',{'context':context})

def aboutPage(request):
    return render(request,'users/about.html')