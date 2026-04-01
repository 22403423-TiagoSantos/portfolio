from django.db import models

class Perfil(models.Model):
    nome = models.CharField(max_length=100)
    titulo_profissional = models.CharField(max_length=100)
    foto_perfil = models.ImageField(upload_to='perfil/')
    biografia = models.TextField()
    link_linkedin = models.URLField(blank=True, null=True)
    link_github = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome