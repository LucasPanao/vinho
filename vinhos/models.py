from django.db import models
from datetime import datetime

class Vinhos(models.Model):
    nomeVinho = models.CharField(max_length=200)
    imagemVinho = models.ImageField(upload_to='.')
    descVinho = models.TextField()
    dataCadastro = models.DateTimeField(default=datetime.now,blank=True) 
