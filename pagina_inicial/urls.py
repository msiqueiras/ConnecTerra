from django.urls import path
from . import views

urlpatterns = [
		path('', views.pagina_inicial, name='pagina_inicial'),
        path('sobre/', views.sobre, name='sobre'),
        path('nossoscontatos/', views.nossos_contatos, name='nossos_contatos')
]