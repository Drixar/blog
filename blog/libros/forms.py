from dataclasses import field, fields
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Resena

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields =['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class FormlarioResena(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ['titulo', 'slug', 'resumen', 'imagen', 'contenido', 'autor', 'categoria', 'usuario', 'estado']