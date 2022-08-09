
from argparse import Namespace
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from prub1.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage,name='homepage'),
    path("register/", include('registrer.urls')),
    path('tienda/',include('tienda.urls',namespace='shopping')),
    path('carro/',include('carro.urls'),name='carro'),
    path('shopp/',include('shopp.urls', namespace='shopp')),
    path('accounts/', include('django.contrib.auth.urls'),name="acounts"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
