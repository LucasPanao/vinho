from django.shortcuts import render, get_list_or_404, get_object_or_404
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

def carrinhovinho(request, vinhos_id):
    vinho = get_object_or_404(Vinhos, pk=vinhos_id)
    vinho_a_exibir = {
        'vinhos' : vinho
    }

    return render(request,'carrinhovinho.html',vinho_a_exibir)