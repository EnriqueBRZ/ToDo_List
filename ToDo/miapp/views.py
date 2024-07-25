from django.shortcuts import render, redirect
from miapp.models import Homework
from miapp.forms import FormHomework, registerForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):

    return render(request, 'index.html', {
        'title': 'Inicio'
    })


@login_required(login_url='login')
def created_task(request):
    
    if request.method == 'POST':
        formulario = FormHomework(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            title = data_form['title']
            content = data_form['content']
            status = data_form['status']

            tarea = Homework(
                title = title,
                description = content,
                status = status
            )

            tarea.save()

            messages.success(request, f'Se ha creado correctamente la tarea {tarea.id}')

            return redirect('tareas')

    else:
        formulario = FormHomework()

    
    return render(request, 'create_task.html', {
        'title': 'Crear Tareas',
        'form': formulario
    })


@login_required(login_url='login')
def taksList(request):

    tareas = Homework.objects.all()

    return render(request, 'lista.html', {
        'title': 'Lista de Tareas',
        'tareas': tareas
    })


@login_required(login_url='login')
def editar_task(request, id):
    
    tarea = Homework.objects.get(pk=id)
    data = {
            'title': tarea.title,
            'content': tarea.description,
            'status': tarea.status
        }

    if request.method == 'POST':
        formulario = FormHomework(request.POST)

        if formulario.is_valid():
            tarea.title = formulario.cleaned_data['title']
            tarea.description = formulario.cleaned_data['content']
            tarea.status = formulario.cleaned_data['status']
            
            tarea.save()

            messages.success(request, f'Se ha guardado la tarea {tarea.id}')

            return redirect('tareas')
        
    else:
        formulario = FormHomework(initial=data)

    return render(request, 'editar_task.html', {
        'title': 'Editar Tarea',
        'form': formulario
    })


@login_required(login_url='login')
def borrar(requets, id):

    tarea =Homework.objects.get(pk=id)
    tarea.delete()

    return redirect('tareas')


def sign_up(request):
    
    if request.user.is_authenticated:
        return redirect('inicio')
    
    else:
    
        register_form = registerForm()

        if request.method == 'POST':
            register_form = registerForm(request.POST)

            if register_form.is_valid():
                register_form.save()

                messages.success(request, 'Te has registrado exitosamente')

                return redirect('inicio')

        return render(request, 'users/signup.html', {
            'title': 'Registrate',
            'form_user': register_form
        })


def login_user(request):

    if request.user.is_authenticated:
        return redirect('inicio')
    
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                messages.warning(request, 'No te has podido indentificar correctamente')

    return render(request, 'users/login.html', {
        'title': 'Identificate'
    })


@login_required(login_url='login')
def logout_user(request):
    logout(request)

    return redirect('login')