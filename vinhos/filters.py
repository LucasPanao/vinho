import django_filters
from .models import Vinhos
class VinhoFilter(django_filters.FilterSet):
    class Meta:
        model = Vinhos
        fields = ['nome_vinho', 'tipo_vinho']