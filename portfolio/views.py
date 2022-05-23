from audioop import reverse
from multiprocessing import context
from django import views
from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime
import datetime





def aboutme_page(request):
	return render(request, 'portfolio/mim.html')


def lincenciatura_page(request):
	return render(request, 'portfolio/licenciatura.html')



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
    query = sorted(PontuacaoQuizz.objects.all(), key=lambda x: x.pontuacao, reverse=True)
    nomes = [objeto.nome for objeto in query]
    pontuacoes = [objeto.pontuacao for objeto in query]
    plt.barh(nomes, pontuacoes)
    plt.savefig('portfolio/static/portfolio/images/grafico.png', bbox_inches='tight')

def home_page_view(request):
	return render(request, 'portfolio/home.html')

def blog_page(request):
  
  
    return render(request, 'portfolio/blog.html')

def resolution_path(instance, filename):
    return f'users/{instance.id}/'
    
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render (request,"users/user.html")

def login_view(request):
    if request.method =='Post':
        username=request.POST['username']
        password=request.POST['password']
        user= authenticate (request,username=username,password=password)

        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, "users/login.html", {
                'message': "Invalid Credentials."
            })
    return render (request,"login.html")

def logout_view(request):
    logout(request)
    return render (request,'login.html', {
        "message": "Logged out."
    })



