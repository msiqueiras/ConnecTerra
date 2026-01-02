from django.shortcuts import render #shortcuts = atalhos

def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')
