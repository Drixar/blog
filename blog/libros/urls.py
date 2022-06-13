from django.urls import path
from .views import home, noticias, resenas, nosotros,contacto, registro, detalleResena

urlpatterns = [
    path('', home, name = 'home'),
    path('noticias/', noticias, name = 'noticias'),
    path('nosotros/', nosotros, name = 'nosotros'),
    path('resenas/', resenas, name = 'resenas'),
    path('contacto/', contacto, name = 'contacto'),
    path('registro/', registro, name = 'registro'),
    path('<slug:slug>/', detalleResena, name = 'detalleResena'),
]