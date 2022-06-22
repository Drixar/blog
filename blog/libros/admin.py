from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class Tema_resource(resources.ModelResource):
    class Meta:
        model = Tema

class Categoria_resource(resources.ModelResource):
    class Meta:
        model = Categoria

class Usuario_resource(resources.ModelResource):
    class Meta:
        model = Usuario

class Post_resource(resources.ModelResource):
    class Meta:
        model = Post

class Comentario_resource(resources.ModelResource):
    class Meta:
        model = Comentario

class Autor_resource(resources.ModelResource):
    class Meta:
        model = Autor

class Resena_resource(resources.ModelResource):
    class Meta:
        model = Post

class Contacto_resource(resources.ModelResource):
    class Meta:
        model = Contacto
class Tema_admin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre'] 
    list_display = ('nombre', 'estado', 'fecha_alta')
    resource_class = Tema_resource

class Categoria_admin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre'] 
    list_display = ('nombre', 'estado', 'fecha_alta')
    resource_class = Categoria_resource

class Usuario_admin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre', 'apellido', 'email']
    list_display = ('nombre', 'apellido', 'estado', 'email', 'fecha_alta')
    resource_class = Usuario_resource

class Post_admin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['titulo', 'resumen', 'contenido']
    list_display = ('titulo', 'estado', 'fecha_alta')
    resource_class = Post_resource

class Autor_admin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre', 'biografia']
    list_display = ('nombre', 'estado', 'fecha_alta')
    resource_class = Autor_resource

class Resena_admin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['titulo', 'autor', 'contenido']
    list_display = ('titulo', 'autor', 'categoria', 'fecha_alta')
    resource_class = Resena_resource

class Comentario_admin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['titulo', 'mensaje']
    list_display = ('titulo', 'usuario', 'resena', 'fecha_alta')
    resource_class = Comentario_resource

class Contacto_admin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre', 'email', 'mensaje']
    list_display = ('nombre', 'email', 'mensaje')
    resource_class = Contacto_resource

admin.site.register(Tema, Tema_admin)
admin.site.register(Categoria, Categoria_admin)
admin.site.register(Usuario, Usuario_admin)
admin.site.register(Post, Post_admin)
admin.site.register(Autor, Autor_admin)
admin.site.register(Resena, Resena_admin)
admin.site.register(Contacto, Contacto_admin)
admin.site.register(Profile)
admin.site.register(Comentario, Comentario_admin)