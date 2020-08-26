from django.contrib import admin
from .models import Vinhos

class listandoVinhos(admin.ModelAdmin):
    list_display = ('id', 'nome_vinho', 'pais_vinho', 'tipo_vinho','casta_vinho', 'ano_vinho', 'refrigerado')
    list_display_links = ('id', 'nome_vinho')
    search_fields = ('nome_vinho',)
    list_filter = ('pais_vinho',)
    list_editable = ('refrigerado',)
    list_per_page = 10
admin.site.register(Vinhos, listandoVinhos)
