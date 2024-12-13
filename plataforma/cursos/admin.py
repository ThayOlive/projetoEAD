
from django.contrib import admin
from .models import Curso, Video, Material
from .forms import CursoAdminForm

class CursoAdmin(admin.ModelAdmin):
    form = CursoAdminForm  # Use o formulário personalizado
    list_display = ['name', 'slug', 'short_description', 'long_description']
    search_fields = ['name', 'slug']
    filter_horizontal = ('videos', 'aluno', 'arquivos')  # Agora arquivos também é gerido pelo Django
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'short_description', 'long_description', 'arquivos', 'videos', 'aluno')
        }),
    )

# Registrando o modelo no admin
admin.site.register(Curso, CursoAdmin)
admin.site.register(Video)
admin.site.register(Material)







