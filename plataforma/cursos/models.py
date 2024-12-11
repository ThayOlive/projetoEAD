from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

class Video(models.Model):
    url = models.URLField("URL do vídeo")
    title = models.CharField("Título do vídeo", max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.title or self.url
    
class Material(models.Model):
    pdf = models.FileField("Material")
    title = models.CharField("Título do arquivo", max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title or self.pdf

    def download_link(self):
        if self.pdf:
            return f'<a href="{self.pdf.url}" target="_blank">Baixar</a>'
        return "Arquivo não disponível"

    download_link.short_description = "Download"
    download_link.allow_tags = True

class Curso(models.Model):
    name = models.CharField(("Curso"), max_length=100)
    slug = models.SlugField(("Categoria"))
    short_description = models.TextField(("Descrição"))
    long_description = models.TextField(("Sobre o curso"))
 
      # Relacionamento de muitos para muitos com arquivos
    arquivos = models.ManyToManyField(Material, related_name="cursos", blank=True)
    
    # Relacionamento de muitos para muitos com vídeos
    videos = models.ManyToManyField(Video, related_name="cursos", blank=True)
    
    aluno = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        verbose_name='Usuário',
        related_name='cursos', 
        blank=True, # Permite que o campo seja opcional
    )

    class Meta:
        verbose_name = ("Curso")
        verbose_name_plural = ("Cursos")

    def __str__(self):
        return self.name
    #def get_absolute_url(self):
      #  return reverse("_detail", kwargs={"pk": self.pk})

        @receiver(post_save, sender= Curso)
        def associar_arquivos(sender, instance, created, **kwargs):
            if created:
         # Aqui você manipula os arquivos após o curso ser salvo no banco de dados
                arquivos = instance.arquivos.all()  # Pode pegar os arquivos associados ao curso
                if arquivos:
            # Isso é apenas um exemplo, dependendo da lógica você pode modificar como associar os arquivos
                 pass  # Associe os arquivos conforme necessário



  