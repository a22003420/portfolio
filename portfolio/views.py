from multiprocessing import context
from django.shortcuts import render
from datetime import datetime
# Create your views here.






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


def home_page_view(request):
	return render(request, 'portfolio/home.html')

def contacto_page_view(request):
	nome="Matos"
	data = datetime.now()

	contexto={"nome":nome, 'hora': data}
	return render(request,'portfolio/contacto.html',contexto)



def footer_page(request):
	return render(request, 'portfolio/rodape.html')