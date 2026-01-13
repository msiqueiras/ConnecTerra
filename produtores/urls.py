from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'), 
    path('produtores/', views.produtoresrurais, name='produtores'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('dashboard/', views.dashboard_produtor, name='dashboard_produtor'),
    path('login/', views.login_produtor, name='login_produtor')   
]