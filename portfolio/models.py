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
    
class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    nivel_dominio = models.IntegerField()
    descricao = models.TextField(blank=True, null=True)

    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='competencias', default=1)

    def __str__(self):
        return self.nome
    
class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    imagem = models.ImageField(upload_to='projetos/')
    link_github = models.URLField(blank=True, null=True)
    
    tecnologias = models.ManyToManyField(Tecnologia, related_name='projetos')
    competencias = models.ManyToManyField(Competencia, related_name='projetos')
    
    unidade_curricular = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE, null=True, blank=True, related_name='projetos')

    def __str__(self):
        return self.nome
    
class Formacao(models.Model):
    nome = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=100)
    data_conclusao = models.DateField(blank=True, null=True)
    logotipo = models.ImageField(upload_to='formacoes/', blank=True, null=True)
    link_certificado = models.URLField(blank=True, null=True)

    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='formacoes', default=1)

    def __str__(self):
        return self.nome
    
class TFC(models.Model):
    nome = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    sumario = models.TextField()
    orientador = models.CharField(max_length=100) 
    classificacao = models.IntegerField()
    
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='tfcs')

    def __str__(self):
        return self.nome
    
class MakingOf(models.Model):
    nome = models.CharField(max_length=100)
    descricao_processo = models.TextField()
    erros_resolucoes = models.TextField()
    imagem = models.ImageField(upload_to='making_of/', blank=True, null=True)

    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='making_ofs', default=1)

    def __str__(self):
        return self.nome