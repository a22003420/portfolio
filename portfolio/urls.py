from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('mim', views.aboutme_page, name='mim'),
    path('licenciatura', views.lincenciatura_page, name='licenciatura'),
    path('blog', views.blog_page, name='blog'),
    path('quizz', views.quizz_page, name='quizz'),
    path('website', views.about_page, name='website'),
] 