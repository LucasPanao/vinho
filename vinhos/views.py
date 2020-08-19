from django.shortcuts import render
from .models import Vinhos

def index(request):
    return render(request,'index.html')

def listavinhos(request):

    vinhos = Vinhos.objects.all()

    dados = {
        'vinhos' : vinhos
    }
    return render(request,'listavinhos.html',dados)