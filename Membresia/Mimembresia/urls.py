from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('about', views.about, name='about'),
    path('membresias', views.membresias, name='membresias'),
    path('museos', views.museos, name='museos'),
    path('contacto', views.contacto, name='contacto')
    

]