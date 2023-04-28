from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.

#Cada tabela/informação nova dentro do banco será uma classe py

#Criar o filme
LISTA_CATEGORIAS = (
    ("ANALISES", "Análises"),
    ("PROGRAMACAO", "Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros"),
)

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=10000)
    categoria = models.CharField(max_length=15, choices =LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self): #qual é o formato de str do objto dessa classe (como ele será exibido ao dar um print)
        return self.titulo


#Criar os episódios - estrutura
# - criação de FK para relacionar filmes a episódios
# A FK deve ser o 1ª campo p/ evitar problemas com BD.
#Parâmetro da fk = nome ta tabela, related_name=, on_delete=

class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):  # qual é o formato de str do objto dessa classe (como ele será exibido ao dar um print)
        return self.filme.titulo + " | " + self.titulo



class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField("Filme")



#Criar o usuario

