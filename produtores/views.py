from django.shortcuts import render, redirect
from produtores.models import ProdutoresRurais
from produtores.forms import ProdutorForm

def produtoresrurais(request):
    produtores = ProdutoresRurais.objects.all().order_by('full_name')
    #parametros de pesquisa
    search = request.GET.get('search')
    if search == None:
        search = ''
    produtores = ProdutoresRurais.objects.filter(city__icontains=search)
    

    return render(request,'catalago_produtores.html',{'produtores': produtores})

def cadastro(request):
    if request.method == 'POST':
        def limpa(campo):
            valor = request.POST.get(campo)
            return valor if valor and valor.strip() else None

        ProdutoresRurais.objects.create(
            full_name=request.POST.get('full_name'),
            cpf=request.POST.get('cpf'),
            cep=request.POST.get('cep'),
            adress=request.POST.get('adress'),
            city=request.POST.get('city'),
            state=request.POST.get('state'),
            email_adress=request.POST.get('email_adress'),
            phone_number=request.POST.get('phone_number'),
            # Aqui está o segredo: se estiver vazio, vira None (NULL no banco)
            employment_name=limpa('employment_name'),
            costume_name=limpa('costume_name'),
            cnpj=limpa('cnpj'),
        )
        return redirect('pagina_inicial')
    
    return render(request, 'cadastro.html')