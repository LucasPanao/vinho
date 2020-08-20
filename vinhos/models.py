from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

## EXTRA FUNCTIONS

def current_year():
    return datetime.datetime.now().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

## EXTRA FUNCTIONS

class Vinhos(models.Model):
    PAISES_VINHO = (
        ("AR", "Argentina"),
        ("AU", "Austrália"),
        ("BR", "Brasil"),
        ("CL", "Chile"),
        ("DE", "Alemanha"),
        ("ES", "Espanha"),
        ("FR", "França"),
        ("IT", "Itália"),
        ("PT", "Portugal"),       
        ("US", "Estados Unidos")
    )

    nome_vinho = models.CharField(max_length=200)
    imagem_vinho = models.ImageField(upload_to='.')
    desc_vinho = models.TextField()
    pais_vinho = models.CharField(max_length=2, choices=PAISES_VINHO)
    produtor_vinho = models.CharField(max_length=200)
    casta_vinho = models.CharField(max_length=200)
    ano_vinho = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1600), max_value_current_year])
    data_cadastro = models.DateTimeField(default=datetime.datetime.now,blank=True) 

    ## EXTRA FUNCTIONS

    def paises_vinho_nomes(self):
        return dict(Vinhos.PAISES_VINHO)[self.pais_vinho]
    
    ## EXTRA FUNCTIONS