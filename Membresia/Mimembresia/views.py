from django.shortcuts import render
from django.http import HttpResponse


def index (request):
    return render(request,'Mimembresia/index.html')

def registro (request):
    return render(request,'Mimembresia/registro.html')



