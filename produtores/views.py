from django.shortcuts import render
from produtores.models import ProdutoresRurais

def produtoresrurais(request):
    produtores = ProdutoresRurais.objects.all().order_by('full_name')
    #parametros de pesquisa
    search = request.GET.get('search')
    if search == None:
        search = ''
    produtores = ProdutoresRurais.objects.filter(city__icontains=search)

    return render(request,'catalago_produtores.html',{'produtores': produtores})
