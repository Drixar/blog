from django.shortcuts import redirect, render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404
from .forms import CustomUserCreationForm, FormularioContacto
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Resena, Contacto
from django.db.models import Q

# Create your views here.

def detalleResena(request, slug):
    try:
        resena = Resena.objects.get(slug = slug)
        return render(request, 'single-post.html', {'resena': resena} )
    except:
        raise Http404("No matches the given query.")

def home(request):
    resenas = Resena.objects.filter(estado = True)
    queryset = request.GET.get("buscar")
    if queryset:
        resenas = Resena.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(contenido__icontains = queryset)
        ).distinct()
    return render(request, 'index.html',{'resenas': resenas})

def noticias(request):
    return render(request, 'noticias.html')

def resenas(request):
    return render(request, 'resenas.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def contacto(request):
    data = {
        'form': FormularioContacto()

    }
    if request.method == 'POST':
        formulario = FormularioContacto(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Mensaje Enviado"
        else:
            data['form'] = formulario
    return render(request, 'contacto.html', data)

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


    