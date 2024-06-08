from django.shortcuts import render
from django.http import HttpResponse
from .forms import*


def index (request):
    return render(request,'Mimembresia/index.html')

def about(request):
    return render(request,"Mimembresia/about.html")

def contacto(request):
    return render(request,"Mimembresia/contacto.html")

def membresias(request):
    return render(request,"Mimembresia/membresias.html")

def museos(request):
    return render(request,"Mimembresia/museos.html")






