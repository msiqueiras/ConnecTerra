from django.urls import path
from . import views

urlpatterns = [
    path('', views.selosverdes, name='selosverdes')
]