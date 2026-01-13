from django.urls import path
from . import views

urlpatterns = [
    path('', views.produtoresrurais, name='produtores'),
    path('cadastro', views.cadastro, name='cadastro')
]

