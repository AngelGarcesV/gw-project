from urllib.request import Request
from django.shortcuts import redirect, render
from shopp.shopp import shoppUser
from carro.carro import carro as carroshop
from django.contrib import messages

# Create your views here.

def registrarCompras(request):
    if request.user.is_authenticated:
        car=carroshop(request=request)
        llaves=car.devolver_datos()
        messages.add_message(request,messages.INFO,llaves)
        if request.method == "POST":
            for prd in llaves:
                ciudad=request.POST['ciudad']
                nombre=request.POST['nombre']
                apellido=request.POST['apellido']
                correo=request.POST['correo']
                telefono=request.POST['telefono']
                direccion=request.POST['direccion']
                compra=shoppUser()
                compra.crear_factura(request.user,prd,ciudad=ciudad,nombre=nombre,apellido=apellido,correo=correo,telefono=telefono,direccion=direccion)
                car.limpiarcarrito()
            return redirect('homepage')
        return render(request,'compras.html')

    
