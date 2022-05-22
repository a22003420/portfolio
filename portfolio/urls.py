from django.urls import path
from . import views


app_name = 'portfolio'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('mim', views.aboutme_page, name='mim'),
    path('projectos', views.projects_page, name='projectos'),
    path('blog', views.blog_page, name='blog'),
    path('quizz', views.quizz_page, name='quizz'),
    path('website', views.about_page, name='website'),
    
    

]
