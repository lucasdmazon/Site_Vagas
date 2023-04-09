from django.contrib import admin
from .models import Categoria, Vaga

class VagaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'nome_empresa', 'descricao_simplificada', 'link', 'curtir')
    list_display_links = ('id', 'titulo', 'nome_empresa', 'curtir')
    list_filter = ('titulo', 'nome_empresa')
    list_per_page = 10
    search_fields = ('titulo', 'nome_empresa', 'curtir')

admin.site.register(Categoria)
admin.site.register(Vaga, VagaAdmin)
