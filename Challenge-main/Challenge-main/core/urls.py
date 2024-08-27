from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('portal_admin', views.admin, name='portal_admin'),
    path('cadastro_geral', views.cadastro_geral, name='cadastro_geral'),
    path('acervo_videos', views.acervo_videos, name='acervo_videos'),
    path('login/', views.login_pagina, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]