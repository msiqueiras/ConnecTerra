from django.urls import path
from . import views

urlpatterns = [ 
    path('catalogo/', views.catalogo, name='catalogo'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('dashboard/', views.dashboard_produtor, name='dashboard_produtor'),
    path('login/', views.login_produtor, name='login_produtor')   
]