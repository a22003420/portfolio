from django.db import models
from matplotlib import pyplot as plt

def resolution_path(instance, filename):
    return f'users/{instance.id}/'


class Pessoa(models.Model):
    nome = models.CharField(max_length=40, unique=True)
    foto = models.ImageField(upload_to=resolution_path) 

class Professor(models.Model):
    nome = models.CharField(max_length=20, unique=True)

class Competencia(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class pontuacao_quizz(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    pontuacao = models.PositiveIntegerField()

class Post (models.Model):
    
     autor=models.CharField(max_length=20)
     data=models.DateField(auto_now_add=True)
     titulo=models.CharField(max_length=20)
     descricao=models.TextField()    
     link=models.URLField(max_length=50,null=True,blank=True)
     docente_teorica = models.ForeignKey(Professor, on_delete=models.CASCADE)

class Cadeira(models.Model):

     CREDITOS = (
        (4, '4 créditos'),
        (5, '5 créditos'),
        (6, '6 créditos'),
        (20,'20 créditos')
        
    )

     SEMESTRE = (
        (1, '1º semestre'),
        (2, '2º semestre'),
    )

     ANO = (
        (1, '1º ano'),
        (2, '2º ano'),
        (3, '3º ano'),
    )

     nome = models.CharField(max_length=20)
     ano = models.IntegerField(choices=ANO,default='1')
     titulo = models.CharField(max_length=50, unique=True)
     descricao = models.TextField(max_length=300)
     competencias = models.ManyToManyField(Competencia) 
     docente= models.ForeignKey(Professor, on_delete=models.CASCADE)
     creditos = models.IntegerField(choices=CREDITOS,default='6')
     semestre= models.PositiveSmallIntegerField(choices=SEMESTRE,default='1')



    
