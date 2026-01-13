from django.db import models

class ProdutoresRurais(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=300, verbose_name='Nome completo do responsável')
    employment_name = models.CharField(max_length=300, verbose_name='Nome da empresa', blank=True, null=True, default='Pessoa Física')
    costume_name = models.CharField(max_length=300, verbose_name='Nome Fantasia da empresa', blank=True, null=True, default='Pessoa Física')
    cpf = models.CharField(max_length=11, unique=True, verbose_name = 'CPF')
    cnpj = models.CharField(max_length=14, unique=True, blank=True, null=True, verbose_name='CNPJ')
    email_adress = models.EmailField(unique=True, verbose_name='Endereço Eletrônico')
    adress = models.CharField(verbose_name='Logradouro com número')
    cep = models.CharField(max_length=8, verbose_name='CEP')
    city = models.CharField(max_length=100, verbose_name='Município', default='Não informado')
    state = models.CharField(max_length=100, default='Não Informado', verbose_name='Estado')
    phone_number = models.CharField(max_length=20, verbose_name='Número de Telefone', unique=True, blank=True, null=True)
    verificate = models.BooleanField(
        default=False, 
        verbose_name='Status de verificação',
        help_text='Marque após a verificação dos dados e certificados do produtor.'
        )

    certificate_upload = models.FileField(
        upload_to='produtores/',
        blank=True,
        null=True,
        verbose_name='Cópia do(s) Certificado(s)'
        )

    selos = models.ManyToManyField(
        'selosverdes.SelosVerdes',
        blank=True,
        verbose_name='Selos Verdes'
        )

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = 'Produtor Rural'
        verbose_name_plural = 'Produtores Rurais'
        ordering = ['full_name']

    # def verificate(self):