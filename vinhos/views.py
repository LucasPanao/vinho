from django.shortcuts import render
from .models import Vinhos

def index(request):
    return render(request,'index.html')

def listavinhos(request):

    vinhos = Vinhos.objects.order_by('-data_cadastro').all()

    dados = {
        'vinhos' : vinhos
    }
    return render(request,'listavinhos.html',dados)

def listavinhosrefrigerados(request):

    vinhos = Vinhos.objects.order_by('-data_cadastro').filter(refrigerado=True)

    dados = {
        'vinhos' : vinhos
    }
    return render(request,'listavinhosrefrigerados.html',dados)