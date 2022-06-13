from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from .forms import CustomUserCreationForm 
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Resena
from django.shortcuts import get_object_or_404
from django.http import Http404

# Create your views here.

def detalleResena(request, slug):
    try:
        resena = Resena.objects.get(slug = slug)
        return render(request, 'single-post.html', {'resena': resena} )
    except:
        raise Http404("No MyModel matches the given query.")

def home(request):
    resenas = Resena.objects.filter(estado = True)
    return render(request, 'index.html',{'resenas': resenas})

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


    