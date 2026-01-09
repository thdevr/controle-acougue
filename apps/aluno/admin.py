from django.contrib import admin
from apps.aluno.models import Aluno


class ListandoAlunos(admin.ModelAdmin):
    list_display = ("id", "nome","matricula", "telefone")
    list_display_links = ("matricula", "nome",)
    search_fields = ("id", "matricula","nome",)
    list_per_page = 10

admin.site.register(Aluno, ListandoAlunos)
