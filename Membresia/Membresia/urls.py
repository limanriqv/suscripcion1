
from django.contrib import admin
from django.urls import path, include
from Mimembresia import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Mimembresia/', include('Mimembresia.urls'))
]
