from django import forms
from django.forms import ClearableFileInput
from .models import Curso, Material

class CursoAdminForm(forms.ModelForm):
    # Adiciona um campo para selecionar arquivos existentes
    arquivos_existentes = forms.ModelMultipleChoiceField(
        queryset=Material.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label="Selecionar arquivos existentes"
    )

    class Meta:
        model = Curso
        fields = '__all__'

    def save(self, commit=True):
        curso = super().save(commit=False)

    # Salve o curso primeiro para garantir que ele tenha um ID
        if commit:
            curso.save()  # Agora o curso tem um ID, pois foi salvo no banco de dados

        # Após salvar o curso, associe os arquivos
            if 'arquivos_existentes' in self.cleaned_data:
                arquivos = self.cleaned_data['arquivos_existentes']
                curso.arquivos.set(arquivos)  # Associe os arquivos ao curso

        return curso