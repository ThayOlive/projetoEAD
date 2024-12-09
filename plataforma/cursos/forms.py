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
    # Salva o curso e associa os arquivos existentes selecionados
        curso = super().save(commit=False)  # Salva o curso sem persistir no banco ainda
        if commit:
            curso.save()  # Salva o curso no banco de dados

        # Adiciona os arquivos selecionados ao ManyToManyField 'arquivos'
        if 'arquivos_existentes' in self.cleaned_data:
            # Combina os arquivos selecionados com os já associados
            curso.arquivos.set(self.cleaned_data['arquivos_existentes'])

        return curso