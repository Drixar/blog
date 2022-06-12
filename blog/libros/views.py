from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from .forms import CustomUserCreationForm 
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'index.html')

def noticias(request):
    return render(request, 'noticias.html')

def resenas(request):
    return render(request, 'resenas.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def contacto(request):
    return render(request, 'contacto.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request,"Te has registrado correctamente")
            return redirect(to='blog:home')
    return render(request, 'registration/registro.html', data)

    