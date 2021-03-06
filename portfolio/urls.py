from django.urls import path
from . import views
from django.conf import *
from django.conf.urls.static import static


app_name = 'portfolio'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('mim', views.aboutme_page, name='mim'),
    path('licenciatura', views.lincenciatura_page, name='licenciatura'),
    path('blog', views.blog_page, name='blog'),
    path('quizz', views.quizz_page, name='quizz'),
    path('website', views.about_page, name='website'),
    path('projectos', views.projectos_page, name='projectos'),
    path('api', views.api_page, name='api'),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)