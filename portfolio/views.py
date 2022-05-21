from multiprocessing import context
from django.shortcuts import render
from datetime import datetime
from matplotlib import pyplot as plt







def aboutme_page(request):
	return render(request, 'portfolio/mim.html')


def projects_page(request):
	return render(request, 'portfolio/projectos.html')


def pw_page(request):
	return render(request, 'portfolio/pw.html')


def blog_page(request):
	
	return render(request, 'portfolio/blog.html')


def about_page(request):
	return render(request, 'portfolio/website.html')

def quizz_page(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        pontos = pontuacao_quizz(request)
        if PontuacaoQuizz.objects.get(nome=nome):
            PontuacaoQuizz.objects.filter(nome=nome).update(pontuacao=pontos)
        else:
            query = PontuacaoQuizz(nome=nome, pontuacao=pontos)
            query.save()
        desenha_grafico_resultados()

    return render(request, 'portfolio/quizz.html')

def pontuacao_quizz(request):
    pontos = 0
    if request.POST['pergunta1'] == 'op2':
        pontos += 25
    if request.POST['pergunta2'] == 'op1':
        pontos += 25
    if request.POST['pergunta3'] == 'op3':
        pontos += 25
    if request.POST['pergunta4'] == 'op3':
        pontos += 25
    return pontos


def desenha_grafico_resultados():
    query = sorted(PontuacaoQuizz.objects.all(), key=lambda x: x.pontuacao, reverse=True)
    nomes = [objeto.nome for objeto in query]
    pontuacoes = [objeto.pontuacao for objeto in query]
    plt.barh(nomes, pontuacoes)
    plt.savefig('portfolio/static/portfolio/images/grafico.png', bbox_inches='tight')

def home_page_view(request):
	return render(request, 'portfolio/home.html')

def contacto_page_view(request):
	nome="Matos"
	data = datetime.now()

	contexto={"nome":nome, 'hora': data}
	return render(request,'portfolio/contacto.html',contexto)



def footer_page(request):
	return render(request, 'portfolio/rodape.html')