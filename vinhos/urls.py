from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listavinhos', views.listavinhos, name='listavinhos'),
    path('listavinhosrefrigerados', views.listavinhosrefrigerados, name='listavinhosrefrigerados')
]