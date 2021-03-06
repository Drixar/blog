from distutils.command.upload import upload
from PIL import Image
from pyexpat import model
from tabnanny import verbose
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.

class Tema(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre del Tema', max_length=30, null=False, blank=False, unique=True)
    estado = models.BooleanField('Activa/Inactiva',default=True)
    fecha_alta = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Tema'
        verbose_name_plural = 'Temas'

    def __str__(self):
        return self.nombre 

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la Categoría', max_length=30, null=False, blank=False, unique=True)
    imagen = models.ImageField(upload_to='images', null=False, blank=False)
    estado = models.BooleanField('Activa/Inactiva',default=True)
    fecha_alta = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre 

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre del Usuario', max_length=30, null=False, blank=False, unique=True)
    apellido = models.CharField('Apellido del Usuario', max_length=30, null=False, blank=False, unique=True)
    estado = models.BooleanField('Activo/Inactivo',default=True)
    email = models.EmailField('Email', blank=False, null=False, unique=True)
    fecha_alta = models.DateField('Fecha de Alta', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return "{0}, {1}".format(self.apellido, self.nombre) 

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Título del Post', max_length=50, null=False, blank=False, unique=True)
    slug = models.SlugField('Slug', max_length=200, null=True, blank=True, unique=True)
    resumen = models.CharField('Resumen del Post', max_length=100, null=False, blank=False, unique=True)
    imagen = models.ImageField(upload_to='images', null=False, blank=False)
    contenido = RichTextField('Contenido')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado',default=True)
    fecha_alta = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo 

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre del Autor', max_length=50, null=False, blank=False, unique=True)
    slug = models.SlugField('Slug', max_length=200, null=True, blank=True, unique=True)
    imagen = models.ImageField(upload_to='images', null=False, blank=False)
    biografia = RichTextField('Biografía', null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado',default=True)
    fecha_alta = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Autor, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre 

class Resena(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Título del Libro', max_length=50, null=False, blank=False, unique=True)
    slug = models.SlugField('Slug', max_length=200, null=True, blank=True, unique=True)
    resumen = models.TextField('Resumen del Post', max_length=200, null=False, blank=False, unique=True)
    imagen = models.ImageField(upload_to='images/', null=False, blank=False)
    contenido = RichTextField('Contenido', null=True, blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado',default=True)
    fecha_alta = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Resena'
        verbose_name_plural = 'Resenas'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Resena, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo 

class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Título del Comentario', max_length=50, null=False, blank=False)
    mensaje = RichTextField('Mensaje', null=False, blank=False)
    usuario = models.CharField('Usuario', max_length=50, null=False, blank=False)
    resena = models.IntegerField('Resena')
    estado = models.BooleanField('Publicado/No Publicado',default=True)
    fecha_alta = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return self.titulo 

class Contacto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre del Remitente', max_length=50, null=False, blank=False, unique=True)
    email = models.EmailField('Email', blank=False, null=False, unique=True)
    asunto = models.CharField('Asunto del Mensaje', max_length=50, null=False, blank=False, unique=True)
    mensaje = models.TextField('Contenido', null=True, blank=True)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.nombre 

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images', null=False, blank=False)

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.avatar.path)
        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

    def __str__(self):
        return self.user.username

