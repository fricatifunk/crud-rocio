from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import especialista
# Create your views here.
from.froms import especialistaForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

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