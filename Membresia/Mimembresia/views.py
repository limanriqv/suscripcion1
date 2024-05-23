from django.shortcuts import render
from django.http import HttpResponse
from .forms import*


def index (request):
    return render(request,'Mimembresia/index.html')

def registro (request):
    contexto = { 'registro_form' : RegistroForm() }
    return render(request,'Mimembresia/registro.html',contexto)





