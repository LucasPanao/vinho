from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('garrafaoutaca', views.garrafaoutaca, name='garrafaoutaca'),
    path('listavinhos', views.listavinhos, name='listavinhos'),
    path('listavinhosrefrigerados', views.listavinhosrefrigerados, name='listavinhosrefrigerados'),
    path('<int:vinhos_id>', views.carrinhovinho, name='carrinhovinho')
]