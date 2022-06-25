from ast import AugStore
from django.shortcuts import redirect, render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404
from platformdirs import user_cache_dir
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Autor, Categoria, Resena, Comentario
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

# Create your views here.

def detalleResena(request, slug):
    lista_categorias = Categoria.objects.filter(estado = True).order_by('nombre')[:20]
    lista_autores = Autor.objects.filter(estado = True).order_by('nombre')[:20]
    resena = get_object_or_404(Resena, slug=slug)
    lista_comentarios = Comentario.objects.filter(estado = True, resena = resena.id ).order_by('-fecha_alta')[:20]
    comentarios =  FormularioComentario(initial={'resena': resena.id, 'usuario': request.user})
    data = {
        'resena': resena,
        'lista_categorias': lista_categorias, 
        'lista_autores': lista_autores,
        'lista_comentarios': lista_comentarios,
        'comentarios': comentarios
        }
    if request.method == 'POST':
        comentarios =  FormularioComentario(data=request.POST)
        if comentarios.is_valid():
            comentarios.save()
            print('pasó')
        else:
            print('no pasó')
    return render(request, 'single-post.html', data)

def agregar_comentario(request, slug):
    lista_categorias = Categoria.objects.filter(estado = True).order_by('nombre')[:20]
    lista_autores = Autor.objects.filter(estado = True).order_by('nombre')[:20]
    resena = get_object_or_404(Resena, slug=slug)
    lista_comentarios = Comentario.objects.filter(estado = True, resena = resena.id ).order_by('-fecha_alta')[:20]
    comentarios =  FormularioComentario(request, initial={'resena': resena_id, 'usuario': request.user})
    data = {
        'resena': resena,
        'lista_categorias': lista_categorias, 
        'lista_autores': lista_autores,
        'lista_comentarios': lista_comentarios,
        'comentarios': comentarios
        }
    if request.method == 'POST':
        comentarios =  FormularioComentario(request.POST)
        # comentarios.resena = resena
        if comentarios.is_valid():
            # comentarios.save()
            messages.success(request,"Comentario publicado correctamente")
            return render(request,"blog:detalleResena",data)
        else:
            data['comentarios'] = comentarios 
    return render(request, 'agregar_comentario.html', data)

def noticias(request):
    return render(request, 'noticias.html')

def resenas(request):
    return render(request, 'resenas.html')

def nosotros(request):
    lista_categorias = Categoria.objects.filter(estado = True).order_by('nombre')[:20]
    lista_autores = Autor.objects.filter(estado = True).order_by('nombre')[:20]
    queryset = request.GET.get("buscar")
    if queryset:
        resenas = Resena.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(contenido__icontains = queryset)
        ).distinct()
        paginator = Paginator(resenas,4)
        pagina = request.GET.get('pagina')
        resenas = paginator.get_page(pagina)
        return render(request, 'resenas/buscar.html',{'resenas': resenas, 'lista_categorias': lista_categorias, 'lista_autores': lista_autores})
    return render(request, 'nosotros.html',{'lista_categorias': lista_categorias, 'lista_autores': lista_autores})

def contacto(request):
    lista_categorias = Categoria.objects.filter(estado = True).order_by('nombre')[:20]
    lista_autores = Autor.objects.filter(estado = True).order_by('nombre')[:20]
    queryset = request.GET.get("buscar")
    if queryset:
        resenas = Resena.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(contenido__icontains = queryset)
        ).distinct()
        paginator = Paginator(resenas,4)
        pagina = request.GET.get('pagina')
        resenas = paginator.get_page(pagina)
        return render(request, 'resenas/buscar.html',{'resenas': resenas, 'lista_categorias': lista_categorias, 'lista_autores': lista_autores})
    data = {
        'form': FormularioContacto(),
        'lista_categorias': lista_categorias, 
        'lista_autores':lista_autores

    }
    if request.method == 'POST':
        formulario = FormularioContacto(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Mensaje Enviado"
        else:
            data['form'] = formulario
    return render(request, 'contacto.html', data)

def index(request):
    resenas = Resena.objects.filter(estado = True).order_by('-fecha_alta')
    lista_categorias = Categoria.objects.filter(estado = True).order_by('nombre')[:20]
    lista_autores = Autor.objects.filter(estado = True).order_by('nombre')[:20]
    queryset = request.GET.get("buscar")
    if queryset:
        resenas = Resena.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(contenido__icontains = queryset)
        ).distinct()
    paginator = Paginator(resenas,4)
    pagina = request.GET.get('pagina')
    resenas = paginator.get_page(pagina)
    return render(request, 'index.html',{'resenas': resenas, 'lista_categorias': lista_categorias, 'lista_autores':lista_autores})

def agregar_autor(request):
    lista_categorias = Categoria.objects.filter(estado = True).order_by('nombre')[:20]
    lista_autores = Autor.objects.filter(estado = True).order_by('nombre')[:20]
    queryset = request.GET.get("buscar")
    if queryset:
        autores = Autor.objects.filter(
            Q(nombre__icontains = queryset) |
            Q(biografia__icontains = queryset)
        ).distinct()
        paginator = Paginator(autores,4)
        pagina = request.GET.get('pagina')
        autores = paginator.get_page(pagina)
        return render(request, 'autor/listar.html',{'autores': autores, 'lista_categorias': lista_categorias, 'lista_autores': lista_autores})
    data = {
    'form': FormularioAutor(),
    'lista_categorias': lista_categorias, 
    'lista_autores':lista_autores
    }
    if request.method == 'POST':
        formulario =  FormularioAutor(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Autor Guardado Correctamente'
            return redirect(to="blog:listar_autor")
        else:
            data['form'] = formulario        
    return render(request, 'autor/agregar.html', data)

@login_required
def listar_autor(request):
    autores = Autor.objects.filter(estado = True).order_by('nombre')
    lista_categorias = Categoria.objects.filter(estado = True).order_by('nombre')[:20]
    lista_autores = Autor.objects.filter(estado = True).order_by('nombre')[:20]
    queryset = request.GET.get("buscar")
    if queryset:
        autores = Autor.objects.filter(
            Q(nombre__icontains = queryset) |
            Q(biografia__icontains = queryset)
        ).distinct()
    paginator = Paginator(autores,4)
    pagina = request.GET.get('pagina')
    autores = paginator.get_page(pagina)
    return render(request, 'autor/listar.html',{'autores': autores, 'lista_categorias': lista_categorias, 'lista_autores': lista_autores})

@staff_member_required
def modificar_autor(request, id):
    lista_categorias = Categoria.objects.filter(estado = True).order_by('nombre')[:20]
    lista_autores = Autor.objects.filter(estado = True).order_by('nombre')[:20]
    queryset = request.GET.get("buscar")
    if queryset:
        autores = Autor.objects.filter(
            Q(nombre__icontains = queryset) |
            Q(biografia__icontains = queryset)
        ).distinct()
        paginator = Paginator(autores,4)
        pagina = request.GET.get('pagina')
        autores = paginator.get_page(pagina)
        return render(request, 'autor/listar.html',{'autores': autores, 'lista_categorias': lista_categorias, 'lista_autores': lista_autores})
    autor = get_object_or_404(Autor, id=id)
    data = {
        'form': FormularioAutor(instance=autor),
        'lista_categorias': lista_categorias, 
        'lista_autores':lista_autores
    }

    if request.method == 'POST':
        formulario =  FormularioAutor(data=request.POST, files=request.FILES, instance=autor)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Autor Modificado Correctamente'
            return redirect(to="blog:listar_autor")
        else:
            data['form'] = formulario  
    return render(request, 'autor/modificar.html', data)

def buscar_autor(request, autor):
    lista_categorias = Categoria.objects.filter(estado = True).order_by('nombre')[:20]
    lista_autores = Autor.objects.filter(estado = True).order_by('nombre')[:20]
    queryset = request.GET.get("buscar")
    if queryset:
        resenas = Resena.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(contenido__icontains = queryset)
        )
        paginator = Paginator(resenas,4)
        pagina = request.GET.get('pagina')
        resenas = paginator.get_page(pagina)
        return render(request, 'resenas/buscar.html',{'resenas': resenas, 'lista_categorias': lista_categorias, 'lista_autores': lista_autores})
    resenas = Resena.objects.filter(
            Q(autor = autor)
        )
    paginator = Paginator(resenas,4)
    pagina = request.GET.get('pagina')
    resenas = paginator.get_page(pagina)
    return render(request, 'autor/buscar.html',{'resenas': resenas, 'lista_categorias': lista_categorias, 'lista_autores': lista_autores})

def mostrar_autor(request, id):
    lista_categorias = Categoria.objects.filter(estado = True).order_by('nombre')[:20]
    lista_autores = Autor.objects.filter(estado = True).order_by('nombre')[:20]
    autor = get_object_or_404(Autor, id=id)
    queryset = request.GET.get("buscar")
    if queryset:
        resenas = Resena.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(contenido__icontains = queryset)
        )
        paginator = Paginator(resenas,4)
        pagina = request.GET.get('pagina')
        resenas = paginator.get_page(pagina)
        return render(request, 'resenas/buscar.html',{'resenas': resenas, 'lista_categorias': lista_categorias, 'lista_autores': lista_autores})
    resenas = Resena.objects.filter(
            Q(autor = autor)
        )
    paginator = Paginator(resenas,4)
    pagina = request.GET.get('pagina')
    resenas = paginator.get_page(pagina)
    return render(request, 'autor/mostrar.html',{'resenas': resenas, 'autor': autor,'lista_categorias': lista_categorias, 'lista_autores': lista_autores})

@staff_member_required
def eliminar_autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    autor.delete()
    return redirect(to='blog:listar_autor')

@staff_member_required
def agregar_categoria(request):
    lista_categorias = Categoria.objects.filter(estado = True).order_by('nombre')[:20]
    lista_autores = Autor.objects.filter(estado = True).order_by('nombre')[:20]
    queryset = request.GET.get("buscar")
    if queryset:
        categorias = Categoria.objects.filter(
            Q(nombre__icontains = queryset) 
        ).distinct()
        paginator = Paginator(categorias,4)
        pagina = request.GET.get('pagina')
        categorias = paginator.get_page(pagina)
        return render(request, 'categoria/listar.html', {'categorias': categorias, 'lista_categorias': lista_categorias, 'lista_autores': lista_autores })
    data = {
    'form': FormularioCategoria(),
    'lista_categorias': lista_categorias, 
    'lista_autores':lista_autores
    }
    if request.method == 'POST':
        formulario =  FormularioCategoria(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Categoría Guardada Correctamente'
            return redirect(to='blog:listar_categoria')
        else:
            data['form'] = formulario  
    return render(request, 'categoria/agregar.html',data)
    
@login_required
def listar_categoria(request):
    lista_categorias = Categoria.objects.filter(estado = True).order_by('nombre')[:20]
    lista_autores = Autor.objects.filter(estado = True).order_by('nombre')[:20]
    categorias = Categoria.objects.filter(estado = True).order_by('nombre')
    queryset = request.GET.get("buscar")
    if queryset:
        categorias = Categoria.objects.filter(
            Q(nombre__icontains = queryset) 
        ).distinct()
    paginator = Paginator(categorias,4)
    pagina = request.GET.get('pagina')
    categorias = paginator.get_page(pagina)
    return render(request, 'categoria/listar.html', {'categorias': categorias, 'lista_categorias': lista_categorias, 'lista_autores': lista_autores })

@staff_member_required
def modificar_categoria(request, id):
    lista_categorias = Categoria.objects.filter(estado = True).order_by('nombre')[:20]
    lista_autores = Autor.objects.filter(estado = True).order_by('nombre')[:20]
    queryset = request.GET.get("buscar")
    if queryset:
        categorias = Categoria.objects.filter(
            Q(nombre__icontains = queryset) 
        ).distinct()
        paginator = Paginator(categorias,4)
        pagina = request.GET.get('pagina')
        categorias = paginator.get_page(pagina)
        return render(request, 'categoria/listar.html', {'categorias': categorias, 'lista_categorias': lista_categorias, 'lista_autores': lista_autores })
    categoria = get_object_or_404(Categoria, id=id)
    data = {
        'form': FormularioCategoria(instance=categoria),
        'lista_categorias': lista_categorias, 
        'lista_autores':lista_autores
    }
    if request.method == 'POST':
        formulario =  FormularioCategoria(data=request.POST, instance=categoria)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Categoría Modificada Correctamente'
            return redirect(to='blog:listar_categoria')
        else:
            data['form'] = formulario  
    return render(request, 'categoria/modificar.html', data)

def buscar_categoria(request, categoria):
    lista_categorias = Categoria.objects.filter(estado = True).order_by('nombre')[:20]
    lista_autores = Autor.objects.filter(estado = True).order_by('nombre')[:20]
    queryset = request.GET.get("buscar")
    if queryset:
        resenas = Resena.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(contenido__icontains = queryset)
        ).distinct()
        paginator = Paginator(resenas,4)
        pagina = request.GET.get('pagina')
        resenas = paginator.get_page(pagina)
        return render(request, 'resenas/buscar.html',{'resenas': resenas, 'lista_categorias': lista_categorias, 'lista_autores': lista_autores})
    resenas = Resena.objects.filter(
            Q(categoria = categoria)
        )
    paginator = Paginator(resenas,4)
    pagina = request.GET.get('pagina')
    resenas = paginator.get_page(pagina)
    return render(request, 'categoria/buscar.html',{'resenas': resenas, 'lista_categorias': lista_categorias, 'lista_autores': lista_autores})

def mostrar_categoria(request, id):
    lista_categorias = Categoria.objects.filter(estado = True).order_by('nombre')[:20]
    lista_autores = Autor.objects.filter(estado = True).order_by('nombre')[:20]
    categoria = get_object_or_404(Categoria, id=id)
    queryset = request.GET.get("buscar")
    if queryset:
        resenas = Resena.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(contenido__icontains = queryset)
        )
        paginator = Paginator(resenas,4)
        pagina = request.GET.get('pagina')
        resenas = paginator.get_page(pagina)
        return render(request, 'resenas/buscar.html',{'resenas': resenas, 'lista_categorias': lista_categorias, 'lista_autores': lista_autores})
    resenas = Resena.objects.filter(
            Q(categoria = categoria)
        )
    paginator = Paginator(resenas,4)
    pagina = request.GET.get('pagina')
    resenas = paginator.get_page(pagina)
    return render(request, 'categoria/mostrar.html',{'resenas': resenas, 'categoria': categoria,'lista_categorias': lista_categorias, 'lista_autores': lista_autores})

@staff_member_required
def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    return redirect(to='blog:listar_categoria')

@staff_member_required
def agregar_resena(request):
    lista_categorias = Categoria.objects.filter(estado = True).order_by('nombre')[:20]
    lista_autores = Autor.objects.filter(estado = True).order_by('nombre')[:20]
    queryset = request.GET.get("buscar")
    if queryset:
        resenas = Resena.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(contenido__icontains = queryset)
        ).distinct()
        paginator = Paginator(resenas,4)
        pagina = request.GET.get('pagina')
        resenas = paginator.get_page(pagina)
        return render(request, 'resenas/listar.html',{'resenas': resenas, 'lista_categorias': lista_categorias, 'lista_autores': lista_autores})
    data = {
    'form': FormularioResena(),
    'lista_categorias': lista_categorias, 
    'lista_autores':lista_autores
    }
    if request.method == 'POST':
        formulario =  FormularioResena(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Reseña Guardada Correctamente'
            return redirect(to='blog:listar_resena')
        else:
            data['form'] = formulario 
    return render(request, 'resenas/agregar.html',data)

@login_required
def listar_resena(request):
    resenas = Resena.objects.filter(estado = True).order_by('titulo')
    lista_categorias = Categoria.objects.filter(estado = True).order_by('nombre')[:20]
    lista_autores = Autor.objects.filter(estado = True).order_by('nombre')[:20]
    queryset = request.GET.get("buscar")
    if queryset:
        resenas = Resena.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(contenido__icontains = queryset)
        ).distinct()
    paginator = Paginator(resenas,4)
    pagina = request.GET.get('pagina')
    resenas = paginator.get_page(pagina)
    return render(request, 'resenas/listar.html',{'resenas': resenas, 'lista_categorias': lista_categorias, 'lista_autores': lista_autores})

@staff_member_required
def modificar_resena(request, id):
    lista_categorias = Categoria.objects.filter(estado = True).order_by('nombre')[:20]
    lista_autores = Autor.objects.filter(estado = True).order_by('nombre')[:20]
    queryset = request.GET.get("buscar")
    if queryset:
        resenas = Resena.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(contenido__icontains = queryset)
        ).distinct()
        paginator = Paginator(resenas,4)
        pagina = request.GET.get('pagina')
        resenas = paginator.get_page(pagina)
        return render(request, 'resenas/listar.html',{'resenas': resenas, 'lista_categorias': lista_categorias, 'lista_autores': lista_autores})
    resena = get_object_or_404(Resena, id=id)
    data = {
        'form': FormularioResena(instance=resena),
        'lista_categorias': lista_categorias, 
        'lista_autores':lista_autores
    }
    if request.method == 'POST':
        formulario =  FormularioResena(data=request.POST, instance=resena, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Reseña Modificada Correctamente'
            return redirect(to='blog:listar_resena')
        else:
            data['form'] = formulario  
    return render(request, 'resenas/modificar.html', data)

@staff_member_required
def eliminar_resena(request, id):
    resena = get_object_or_404(Resena, id=id)
    resena.delete()
    return redirect(to='blog:listar_resena')

def iniciar_sesion(request):
    lista_categorias = Categoria.objects.filter(estado = True).order_by('nombre')[:20]
    lista_autores = Autor.objects.filter(estado = True).order_by('nombre')[:20]
    queryset = request.GET.get("buscar")
    if queryset:
        resenas = Resena.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(contenido__icontains = queryset)
        ).distinct()
        paginator = Paginator(resenas,4)
        pagina = request.GET.get('pagina')
        resenas = paginator.get_page(pagina)
        return render(request, 'resenas/buscar.html',{'resenas': resenas, 'lista_categorias': lista_categorias, 'lista_autores': lista_autores})
    form = AuthenticationForm(request, data = request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request,"Has ingresado correctamente")
        return redirect(to='blog:index')
    else:
        form = AuthenticationForm(request)
        data = {
        'form': FormularioContacto(),
        'lista_categorias': lista_categorias, 
        'lista_autores':lista_autores

        }
    return render(request, "registration/login.html", data)

def crear_usuario(request):
    lista_categorias = Categoria.objects.filter(estado = True).order_by('nombre')[:20]
    lista_autores = Autor.objects.filter(estado = True).order_by('nombre')[:20]
    queryset = request.GET.get("buscar")
    if queryset:
        resenas = Resena.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(contenido__icontains = queryset)
        )
        paginator = Paginator(resenas,4)
        pagina = request.GET.get('pagina')
        resenas = paginator.get_page(pagina)
        return render(request, 'resenas/buscar.html',{'resenas': resenas, 'lista_categorias': lista_categorias, 'lista_autores': lista_autores})
    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        profile_form = CreateProfileForm(request.POST, request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            # profile_form = UpdateProfileForm(request.POST, request.FILES)
            user = authenticate(username=user_form.cleaned_data["username"], password=user_form.cleaned_data["password1"])
            login(request, user)
            user = User.objects.get(id=user.id)
            profile_form.instance.user = user
            profile_form.save()
            messages.success(request,"Te has registrado correctamente")
            return redirect(to='blog:index')
    user_form = CreateUserForm(data=request.POST)
    profile_form = CreateProfileForm(data=request.POST, files=request.FILES)
    return render(request, 'registration/registro.html', {'user_form': user_form, 'profile_form': profile_form, 'lista_categorias': lista_categorias, 'lista_autores': lista_autores})

@login_required
def modificar_usuario(request):
    lista_categorias = Categoria.objects.filter(estado = True).order_by('nombre')[:20]
    lista_autores = Autor.objects.filter(estado = True).order_by('nombre')[:20]
    queryset = request.GET.get("buscar")
    if queryset:
        resenas = Resena.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(contenido__icontains = queryset)
        )
        paginator = Paginator(resenas,4)
        pagina = request.GET.get('pagina')
        resenas = paginator.get_page(pagina)
        return render(request, 'resenas/buscar.html',{'resenas': resenas, 'lista_categorias': lista_categorias, 'lista_autores': lista_autores})
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        print(user_form.is_valid(), profile_form.is_valid())
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Tu perfil se modificó correctamente')
            return redirect(to='blog:index')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'registration/modificar.html', {'user_form': user_form, 'profile_form': profile_form, 'lista_categorias': lista_categorias, 'lista_autores': lista_autores})