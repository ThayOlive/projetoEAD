from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    aluno = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(("Curso"), max_length=100)
    slug = models.SlugField(("Categoria"))
    short_description = models.TextField(("Descrição"))
    long_description= models.TextField(("Sobre o curso"))

    class Meta:
        verbose_name = ("Curso")
        verbose_name_plural = ("Cursos")

    def __str__(self):
        return self.name

    #def get_absolute_url(self):
      #  return reverse("_detail", kwargs={"pk": self.pk})

  