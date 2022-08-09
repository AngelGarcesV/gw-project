import email
from django.contrib import admin

# Register your models here.
from database.models import user, producto, factura, factura_producto

class userAdmin(admin.ModelAdmin):
    list_display=('username','email','is_staff','is_active')
    search_fields=("username","email")
    list_filter=("is_staff",'is_active',)

class prodAdmin(admin.ModelAdmin):
    list_display=('nombre_producto','category','stock','precio_unitario')
    search_fields=("nombre_producto","category")
    list_filter=('category','stock','precio_unitario',)

class factAdmin(admin.ModelAdmin):
    list_display=('ID_factura','estado','Id_cliecte_id','fecha')
    search_fields=('Id_cliecte_id','ID_factura')
    list_filter=('estado','fecha',)

class factAdminProd(admin.ModelAdmin):
    list_display=('ID_facPro','cantidad','Id_factura_id','Id_producto_id')
    search_fields=("ID_facPro'","Id_factura_id")
    list_filter=('cantidad',)

admin.site.register(user,userAdmin)
admin.site.register(producto,prodAdmin)
admin.site.register(factura,factAdmin)
admin.site.register(factura_producto,factAdminProd)
