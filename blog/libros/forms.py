from dataclasses import field, fields
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Resena, Contacto, Autor, Categoria,Profile, Comentario, Usuario
from ckeditor.widgets import CKEditorWidget


class FormularioResena(forms.ModelForm):
    resumen = forms.CharField(max_length=300, required=True, widget=forms.Textarea(
        attrs={'class': 'form-control','rows': 3, 'placeholder': "Ingrese el Resumen de la Reseña"}))
    titulo = forms.CharField(max_length=50, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Ingrese el título para su Reseña"}))
    slug = forms.SlugField(max_length=50, required=False, widget=forms.HiddenInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Resena
        fields = '__all__'
class FormularioComentario(forms.ModelForm):
    titulo = forms.CharField(max_length=50, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Ingrese el título para su comentario"}))
    mensaje = forms.CharField(max_length=300, required=True, widget=forms.Textarea(
        attrs={'class': 'form-control','rows': 3, 'placeholder': "Ingrese el Título su comentario"}))
    usuario = forms.CharField(max_length=50, widget=forms.HiddenInput(attrs={'class': 'form-control'}))
    resena = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Comentario
        fields = '__all__'
class FormularioContacto(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

class FormularioCategoria(forms.ModelForm):
    nombre = forms.CharField(max_length=30, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Ingrese el Nombre de la Categoría"}))
    class Meta:
        model = Categoria
        fields = '__all__'
class FormularioAutor(forms.ModelForm):
    
    slug = forms.SlugField(max_length=50, required=False, widget=forms.HiddenInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Autor
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Ingrese su Nombre de Usuario"}))
    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Ingrese el Correo Electrónico"}))
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Ingrese su Nombre"}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Ingrese su Apellido"}))
    password1 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': "Ingrese Su Contraseña"}))
    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': "Repita su Contraseña"}))
    class Meta:
        model = User
        fields =['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class CreateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    class Meta:
        model = Profile
        fields = ['avatar']
class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    class Meta:
        model = Profile
        fields = ['avatar']