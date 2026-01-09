from django.contrib import admin
from .models import Produto

class ListandoProdutos(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'quantidade_kg', 'preco_por_kg', 'data_validade')
    list_display_links = ('codigo', 'nome')
    search_fields = ('codigo', 'nome')
    list_per_page = 10  # quantidade de itens por página

admin.site.register(Produto, ListandoProdutos)

