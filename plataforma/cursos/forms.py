from django import forms
from .models import Curso, Material

class CursoAdminForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

    def save(self, commit=True):
        curso = super().save(commit=False)

        if commit:
            curso.save()

        return curso