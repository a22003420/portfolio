from django.urls import path
from . import views


app_name = 'portfolio'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('contacto', views.contacto_page_view, name='contacto'),

    path('mim', views.aboutme_page, name='mim'),
    path('projectos', views.projects_page, name='projectos'),
    path('pw', views.pw_page, name='pw'),
    path('blog', views.blog_page, name='blog'),
    path('website', views.about_page, name='website'),
    path('rodape', views.footer_page, name='rodape'),
    

]
