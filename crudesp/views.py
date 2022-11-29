from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import especialista
# Create your views here.
from.forms import especialistaForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

def inicio(request):
    return render(request,'paginas/inicio.html')

def nosotros(request):
    return render(request,'paginas/nosotros.html')

#funciones de crud
def emp (request):
    emp= especialista.objects.all()
    print(especialista)
    return render(request,'emp/index.html',{'emp':emp})

def empleados (request):
    emp= especialista.objects.all()
    print(especialista)
    return render(request,'emp/index2.html',{'emp':emp})


def crearemp (request):
    formulario=especialistaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('emp')

    return render(request,'emp/crear.html', {'formulario':formulario}) 

def editaremp (request,id):
    Especialista=especialista.objects.get(id=id)
    formulario=especialistaForm(request.POST or None, request.FILES or None, instance=Especialista)
    return render(request, 'emp/editar.html', {'formulario':formulario})
   


def eliminar (request, id):
    Especialista=especialista.objects.get(id=id)
    Especialista.delete()
    return redirect ('emp')





def registro (request):

    if request.method =='POST':
        form = UserCreationForm (request.POST)
        if form.is_valid():
            usuario=form.save()
            login (request,usuario)
            return redirect('emp')
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])



    form=UserCreationForm
    return render(request,'emp/registro.html',{"form":form})