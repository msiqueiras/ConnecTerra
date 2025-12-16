from django.contrib import admin
from produtores.models import ProdutoresRurais

class ProdutoresRuraisAdmin(admin.ModelAdmin):

    def format_selos(self, produtor):
        selos_verdes = []
        for selo in produtor.selos.all():
            selos_verdes.append(selo.name)
        return ', '.join(selos_verdes)

    format_selos.short_description = 'Selos Certificados'
    
    list_display = ('full_name', 'email_adress', 'phone_number', 'cep', 'format_selos', 'verificate')
    search_fields = ('full_name', 'email_adress', 'selo__name')
    list_filter = ('verificate', 'selos')


admin.site.register(ProdutoresRurais, ProdutoresRuraisAdmin)