from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name = 'index'),
    path('noticias/', noticias, name = 'noticias'),
    path('nosotros/', nosotros, name = 'nosotros'),
    path('resenas/', resenas, name = 'resenas'),
    path('contacto/', contacto, name = 'contacto'),
    path('crear-usuario/', crear_usuario, name = 'crear_usuario'),
    path('iniciar-sesion/', iniciar_sesion, name = 'iniciar_sesion'),
    path('modificar-usuario/', modificar_usuario, name = 'modificar_usuario'),
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html')),
    path('agregar-autor/', agregar_autor, name= 'agregar_autor'),
    path('listar-autor/', listar_autor, name= 'listar_autor'),
    path('modificar-autor/<id>/', modificar_autor, name= 'modificar_autor'),
    path('mostrar-autor/<id>/', mostrar_autor, name= 'mostrar_autor'),
    path('buscar-autor/<autor>/', buscar_autor, name= 'buscar_autor'),
    path('eliminar-autor/<id>/', eliminar_autor, name= 'eliminar_autor'),
    path('agregar-categoria/', agregar_categoria, name= 'agregar_categoria'),
    path('listar-categoria/', listar_categoria, name= 'listar_categoria'),
    path('modificar-categoria/<id>/', modificar_categoria, name= 'modificar_categoria'),
    path('mostrar-categoria/<id>/', mostrar_categoria, name= 'mostrar_categoria'),
    path('buscar-categoria/<categoria>/', buscar_categoria, name= 'buscar_categoria'),
    path('eliminar-categoria/<id>/', eliminar_categoria, name= 'eliminar_categoria'),
    path('agregar-resena/', agregar_resena, name= 'agregar_resena'),
    path('listar-resena/', listar_resena, name= 'listar_resena'),
    path('modificar-resena/<id>/', modificar_resena, name= 'modificar_resena'),
    path('eliminar-resena/<id>/', eliminar_resena, name= 'eliminar_resena'),
    path('agregar-comentario/<slug>/', agregar_comentario, name= 'agregar_comentario'),
    path('<slug:slug>/', detalleResena, name = 'detalleResena'),
]
