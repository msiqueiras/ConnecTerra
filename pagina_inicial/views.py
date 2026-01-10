from django.shortcuts import render #shortcuts = atalhos

def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')

def sobre(request):
    return render(request, 'sobre.html')

def nossos_contatos(request):
    return render(request, 'nossoscontatos.html')