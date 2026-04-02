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
    
class Licenciatura(models.Model):
    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE, related_name='licenciatura')
    
    nome = models.CharField(max_length=200)
    ects_totais = models.IntegerField()
    descricao = models.TextField()
    link_plano_estudos = models.URLField()

    def __str__(self):
        return self.nome
    
class Docente(models.Model):
    nome = models.CharField(max_length=100)
    link_pagina_pessoal = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome
    
class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=200)
    ects = models.IntegerField()
    imagem = models.ImageField(upload_to='ucs/', blank=True, null=True)
    ano_semestre = models.CharField(max_length=50)
    
    docentes = models.ManyToManyField(Docente, related_name='ucs')
    licenciaturas = models.ManyToManyField(Licenciatura, related_name='ucs')

    def __str__(self):
        return self.nome
    
class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='tecnologias/', blank=True, null=True)
    link_tecnologia = models.URLField(blank=True, null=True)
    descricao = models.TextField()
    nivel_interesse = models.IntegerField()

    def __str__(self):
        return self.nome