from database.models import factura, factura_producto
from database.models import producto as prd
from carro.carro import carro
class shoppUser():

    def crear_factura(self,user, productoid,ciudad,nombre,apellido,correo,telefono,direccion):
        
        productoU=prd.objects.filter(ID_producto=productoid[0])

        producto=factura()
        producto.Id_cliecte=user
        producto.estado="activo"
        producto.forma_pago="tarjeta"
        producto.ciudad=ciudad
        producto.nombre=nombre
        producto.apellido=apellido
        producto.correo=correo
        producto.telefono=telefono
        producto.direccion=direccion
        producto.valor_compra=productoid[2]
        producto.save()

        factura_prod=factura_producto()
        factura_prod.cantidad=productoid[1]
        factura_prod.Id_factura=producto
        factura_prod.Id_producto=productoU[0]
        
        factura_prod.save()

