from django.shortcuts import render, redirect
from produtores.models import ProdutoresRurais
from produtores.forms import ProdutorForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required 

def catalogo(request):
    search = request.GET.get('search', '').strip()
    
    if search:
        produtores = ProdutoresRurais.objects.filter(city__icontains=search).order_by('full_name')
    else:
        produtores = ProdutoresRurais.objects.all().order_by('full_name')
    
    return render(request, 'catalogo_produtores.html', {'catalogo': produtores})

def cadastro(request):
    if request.method == 'POST':
        email = request.POST.get('email_adress')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirmar_senha')
        cpf = request.POST.get('cpf')
        nome_completo = request.POST.get('full_name')
        logradouro = request.POST.get('adress')
        
        if senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem!')
            return render(request, 'cadastro.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Este email já está cadastrado!')
            return render(request, 'cadastro.html')
        
        if ProdutoresRurais.objects.filter(cpf=cpf).exists():
            messages.error(request, 'Este CPF já está cadastrado!')
            return render(request, 'cadastro.html')
        
        user = User.objects.create(
            username=email, 
            email=email,
            first_name=nome_completo.split()[0] if nome_completo else '',
            last_name=' '.join(nome_completo.split()[1:]) if len(nome_completo.split()) > 1 else ''
        )
        user.set_password(senha)
        user.save()
        
        def limpa(campo):
            valor = request.POST.get(campo)
            return valor if valor and valor.strip() else None

        ProdutoresRurais.objects.create(
            user=user, 
            full_name=nome_completo,
            cpf=cpf,
            cep=request.POST.get('cep'),
            adress=request.POST.get('adress'),
            city=request.POST.get('city'),
            state=request.POST.get('state'),
            email_adress=email,
            phone_number=request.POST.get('phone_number'),
            employment_name=limpa('employment_name'),
            costume_name=limpa('costume_name'),
            cnpj=limpa('cnpj'),
        )
        
        messages.success(request, 'Cadastro realizado com sucesso! Faça login para continuar.')
        return redirect('login_produtor')
    
    return render(request, 'cadastro.html')



def login_produtor(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = authenticate(request, username=email, password=senha)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Bem-vindo, {user.first_name}!')
            return redirect('dashboard_produtor')
        else:
            messages.error(request, 'Email ou senha incorretos!')
    
    return render(request, 'login.html')


@login_required(login_url='login_produtor')
def dashboard_produtor(request):
    try:
        produtor = request.user.produtoresrurais
    except ProdutoresRurais.DoesNotExist:
        messages.error(request, 'Produtor não encontrado!')
        return redirect('login_produtor')
    
    if request.method == 'POST':
        
        novo_cnpj = request.POST.get('cnpj', '').strip()
        novo_telefone = request.POST.get('telefone', '').strip()
        
        if not novo_cnpj:
            produtor.cnpj = None
        else:
            if ProdutoresRurais.objects.filter(cnpj=novo_cnpj).exclude(id=produtor.id).exists():
                messages.error(request, 'Este CNPJ já está cadastrado!')
                return redirect('dashboard_produtor')
            produtor.cnpj = novo_cnpj


        if novo_telefone != produtor.phone_number:
            if ProdutoresRurais.objects.filter(phone_number=novo_telefone).exists():
                messages.error(request, 'Este número de telefone já está cadastrado por outro produtor')
                return redirect('dashboard_produtor')
            produtor.phone_number = novo_telefone
        
        if 'certificate_upload' in request.FILES:
            produtor.certificate_upload = request.FILES['certificate_upload']

        #as infos pessoais q podem ser alteradas
        produtor.cep = request.POST.get('cep')
        produtor.adress = request.POST.get('logradouro')
        produtor.city = request.POST.get('cidade')
        produtor.state = request.POST.get('estado')
        
        #adição de infos de empresas
        produtor.employment_name = request.POST.get('nome_empresa', '')
        produtor.costume_name = request.POST.get('nome_fantasia', '')

        produtor.save()
        
        messages.success(request, 'Informações e certificações atualizadas com sucesso!')
        return redirect('dashboard_produtor')
    
    context = {
        'produtor': produtor,
    }
    
    return render(request, 'dashboard.html', context)