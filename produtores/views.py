from django.shortcuts import render
from produtores.models import ProdutoresRurais

def produtoresrurais(request):
    produtores = ProdutoresRurais.objects.all()

    return render(request,'catalago_produtores.html',{'produtores': produtores})
