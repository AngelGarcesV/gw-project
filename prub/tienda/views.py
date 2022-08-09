from django.shortcuts import render,redirect
from database.models import producto
from django.contrib import messages

encoding="utf-8"
# Create your views here.

def inventario(request,filtro):
    productos=producto.objects.filter(category=filtro)
    return render(request,'tienda.html', {'productos':productos})

def ver_producto(request, productoid):
    productoUni=producto.objects.filter(ID_producto=productoid)
    if productoUni:
        return render(request,'producto.html', {'productos':productoUni})
    return redirect("tienda")


