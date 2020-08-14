from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def listavinhos(request):

    vinhos = {
        1:'Vinho Rapariga',
        2:'Vinho Rapariga 2',
        3:'Vinho Rapariga 3'
    }
    dados = {
        'nomeVinho' : vinhos
    }
    return render(request,'listavinhos.html',dados)