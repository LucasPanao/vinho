from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def listavinhos(request):
    return render(request,'listavinhos.html')