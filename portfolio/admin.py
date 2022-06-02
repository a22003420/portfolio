from django.contrib import admin
from .models import *

class CadeiraAdmin(admin.ModelAdmin):

    list = ('nome' 'ano', 'semestre', 'creditos')
    search_list = ('nome' 'ano', 'semestre', 'creditos')
    

class PessoaAdmin(admin.ModelAdmin):
    list = ('nome',)
    search_list = ['nome'] 

class TecnologiaAdmin(admin.ModelAdmin):
    list = ('nome',)
    search_list = ['nome']


class PostAdmin (admin.ModelAdmin):

    list = ('autor', 'data', 'titulo','descricao')
    search_list = ['autor', 'data', 'titulo','descricao']

class TfcsDeisiAdmin (admin.ModelAdmin):
    list = ('autor', 'data', 'titulo','resumo')
    search_list = ['autor', 'data', 'titulo','resumo']


class CompetenciaAdmin(admin.ModelAdmin):
    list = ('nome',)
    search_list= ['nome']


admin.site.register(Cadeira, CadeiraAdmin)
admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Competencia, CompetenciaAdmin)
admin.site.register(Tecnologia, TecnologiaAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(TfcsDeisi, TfcsDeisiAdmin)

