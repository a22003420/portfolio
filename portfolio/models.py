from django.db import models

# Create your models here.

class Post (models.Model):
    
     autor=models.CharField(max_length=20)
     data=models.DateField(auto_now_add=True)
     titulo=models.CharField(max_length=20)
     descricao=models.TextField()    
     link=models.URLField(max_length=30,null=True,blank=True)

