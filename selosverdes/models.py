from django.db import models
from django.utils.text import slugify

class SelosVerdes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, verbose_name='Nome do Selo Verde')
    issuing_body = models.CharField(max_length=200, blank=True, null=True, verbose_name='Órgão Emissor')
    description = models.TextField(verbose_name='Descrição do Selo')
    official_link = models.URLField(blank=True, null=True, verbose_name='Link Oficial')
    file_name_logo = models.ImageField(upload_to='selosverdes/', blank=True, null=True, verbose_name='Logo do Selo (upload)')
    slug = models.SlugField(max_length=150, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Selo Verde'
        verbose_name_plural = 'Selos Verdes'
        ordering = ['name']