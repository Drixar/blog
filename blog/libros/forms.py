from dataclasses import field, fields
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Resena, Contacto, Autor, Categoria
from ckeditor.widgets import CKEditorWidget

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields =['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class FormularioResena(forms.ModelForm):
    class Meta:
        model = Resena
        fields = '__all__'

class FormularioContacto(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

class FormularioCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class FormularioAutor(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'