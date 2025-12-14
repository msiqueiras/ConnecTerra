from django.contrib import admin
from selosverdes.models import SelosVerdes

class SelosVerdesAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuing_body', 'official_link', 'slug')
    search_fields = ('name', 'issuing_body')

admin.site.register(SelosVerdes, SelosVerdesAdmin)
