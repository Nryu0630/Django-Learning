from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return render(request,'hello.html',{'name':'123'})