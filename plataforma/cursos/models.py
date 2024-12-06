from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import get_user_model

class Curso(models.Model):
    name = models.CharField(("Curso"), max_length=100)
    slug = models.SlugField(("Categoria"))
    short_description = models.TextField(("Descrição"))
    long_description= models.TextField(("Sobre o curso"))
    pdf = models.FileField(("Material"))
    video_aula = models.URLField(("Vídeo"))
    
    aluno = models.ForeignKey(
        settings.AUTH_USER_MODEL,
            verbose_name='Usuário',
            on_delete = models.CASCADE,
            related_name='enrollments', default=True)
    


    class Meta:
        verbose_name = ("Curso")
        verbose_name_plural = ("Cursos")

    def __str__(self):
        return self.name

    #def get_absolute_url(self):
      #  return reverse("_detail", kwargs={"pk": self.pk})



  