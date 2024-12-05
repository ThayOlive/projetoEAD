from django.contrib import admin

from .models import Curso

admin.site.register(Curso)

class CursoAdmin(admin.ModelAdmin):
    list_display = ("name", "short_description")
    filter_horizontal = ("alunos",)  # Interface mais amigável para gerenciar alunos associados

