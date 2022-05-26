from django.urls import reverse
from multiprocessing import context
from pickle import NONE
from django import views
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from datetime import datetime
import datetime
from matplotlib import pyplot as plt
from django.contrib.auth import authenticate,login,logout
from . models import *

def aboutme_page(request):
	return render(request, 'portfolio/mim.html')


def lincenciatura_page(request):

    contexto = {"cadeiras":Cadeira.objects.all()}

    return render(request, 'portfolio/licenciatura.html',contexto)



def about_page(request):
    now = datetime.datetime.now()
    local = "Lisboa, Portugal Continental"

    context = {
        'dataHora': now,
        'local': local
    }

    return render(request, 'portfolio/website.html', context)



def quizz_page(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        pontos = pontuacao_quizz_function(request)
        if pontuacao_quizz.objects.filter(nome=nome).exists():
            pontuacao_quizz.objects.filter(nome=nome).update(pontuacao=pontos)
        else:
            query = pontuacao_quizz(nome=nome, pontuacao=pontos)
            query.save()
        desenha_grafico_resultados()
        return redirect (reverse('portfolio:quizz'))

    return render(request, 'portfolio/quizz.html')

def pontuacao_quizz_function(request):
    pontos = 0
    if request.POST['question1'] == 'q2':
        pontos += 25
    if request.POST['question2'] == 'q1':
        pontos += 25
    if request.POST['question3'] == 'q3':
        pontos += 25
    if request.POST['question4'] == 'q3':
        pontos += 25
    return pontos


def desenha_grafico_resultados():
    query = sorted(pontuacao_quizz.objects.all(), key=lambda x: x.pontuacao, reverse=True)
    nomes = [objeto.nome for objeto in query]
    pontuacoes = [objeto.pontuacao for objeto in query]
    plt.barh(nomes, pontuacoes)
    plt.savefig('portfolio/static/portfolio/images/grafico.png', bbox_inches='tight')
    plt.close()
    
def home_page_view(request):
	return render(request, 'portfolio/home.html')

def blog_page(request):

    if request.method == 'POST':
        nome = request.POST['name']
        titulo = request.POST['subject']
        texto = request.POST['text']
        imagem = request.FILES.get('image',None)



        post=Post(autor=nome,titulo=titulo,descricao=texto,foto=imagem)
        post.save()
    
    contexto = {"posts":Post.objects.all()}
    
    return render(request, 'portfolio/blog.html',contexto)





