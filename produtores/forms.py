from django import forms


class ProdutorForm(forms.Form):
    full_name = forms.CharField(max_length=300, label = 'Nome completo do responsável*')
    employment_name = forms.CharField(max_length=300, label='Nome da empresa', required=False)
    costume_name = forms.CharField(max_length=300, label='Nome fantasia da empresa', required=False)
    cpf = forms.CharField(max_length=11, label ='CPF*')
    cnpj = forms.CharField(max_length=14, label ='CNPJ', required=False)
    email_adress = forms.EmailField(label='Endereço Eletrônico*')
    adress = forms.CharField(label='Logradouro com número*', widget=forms.Textarea)
    cep = forms.CharField(max_length=8, label='CEP*')
    city = forms.CharField(max_length=100, label='Município*')
    state = forms.CharField(max_length=100, label='Estado*')
    phone_number = forms.CharField(max_length=20, label='Número de Telefone')
    certificate_upload = forms.FileField(label='Cópia do(s) Certificado(s)', required=False)
    summary_prod = forms.CharField(widget=forms.Textarea)
