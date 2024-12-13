
from django.contrib import admin
from .models import Curso, Video, Material
from .forms import CursoAdminForm

class CursoAdmin(admin.ModelAdmin):
    form = CursoAdminForm
    list_display = ['name', 'slug', 'short_description', 'long_description']
    search_fields = ['name', 'slug']
    filter_horizontal = ('videos', 'aluno') # Não inclui 'arquivos' porque é gerenciado manualmente
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'short_description', 'long_description', 'arquivos_existentes', 'videos', 'aluno')
        }),
    )

class MaterialAdmin(admin.ModelAdmin):
    list_display = ['title']


# Registrando o modelo no admin
admin.site.register(Curso, CursoAdmin)
admin.site.register(Video)
admin.site.register(Material, MaterialAdmin)







