from email.policy import default
from django.db import models


def resolution_path(instance, filename):
    return 'images/{0}/'.format(filename)


class Pessoa(models.Model):
    nome = models.CharField(max_length=40, unique=True)
    webPage = models.URLField(null=True,blank=True)

class Tecnologia(models.Model):
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
     link=models.URLField(null=True,blank=True)
     foto = models.ImageField(upload_to=resolution_path,default="foto.png")

class TfcsDeisi (models.Model):

        ANO = (
        (2020, '2020'),
        (2021, '2021'),
        (2022, '2022'),
    )
    
        autor=models.CharField(max_length=20)
        orientador=models.CharField(max_length=20)
        ano=models.IntegerField(choices=ANO,default='2021')
        titulo=models.CharField(max_length=20)
        resumo=models.TextField()    
        link=models.URLField(null=True,blank=True)
        relatorio=models.TextField()  
        imagem = models.ImageField(upload_to=resolution_path,default="imagem.png")

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



     nome = models.CharField(max_length=100)
     ano = models.IntegerField(choices=ANO,default='1')
     titulo = models.CharField(max_length=50, unique=True)
     ranking = models.PositiveIntegerField(default=3)
     descricao = models.TextField(max_length=300)
     competencias = models.ManyToManyField(Competencia) 
     docente= models.ForeignKey(Pessoa, on_delete=models.CASCADE)
     creditos = models.IntegerField(choices=CREDITOS,default='6')
     semestre= models.PositiveSmallIntegerField(choices=SEMESTRE,default='1')



    
