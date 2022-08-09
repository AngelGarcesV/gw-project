from django.urls import path
from django.contrib.auth.urls import urlpatterns
from login.views import logueando

urlpatterns = [
    path('', logueando, name="logueando")    
]