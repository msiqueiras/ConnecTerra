from django.db import models

class ProdutoresRurais(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=300, verbose_name='Nome completo')
    cpf = models.CharField(max_length=11, unique=True, verbose_name = 'CPF')
    cnpj = models.CharField(max_length=14, unique=True, blank=True, null=True, verbose_name='CNPJ')
    email_adress = models.EmailField(unique=True, verbose_name='Endereço Eletrônico')
    adress = models.TextField(verbose_name='Endereço Completo')
    cep = models.CharField(max_length=8, verbose_name='CEP')
    phone_number = models.CharField(max_length=20, verbose_name='Número de Telefone', unique=True, blank=True, null=True)
    verificate = models.BooleanField(
        default=False, 
        verbose_name='Status de verificação',
        help_text='Marque após a verificação dos dados e certificados do produtor.'
        )

    certificate_upload = models.FileField(
        upload_to='certificados/',
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