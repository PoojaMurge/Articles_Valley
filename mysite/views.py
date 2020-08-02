#from django.http import HttpRespone
from django.shortcuts import render

def homepage(request):
    #return HttpRespone('homepage')
    return render(request,'homepage.html')

def about(request):
    #return HttpRespone('about') 
    return render(request,'about.html')