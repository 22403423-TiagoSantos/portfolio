from django.contrib import admin
from .models import Perfil, Licenciatura, Docente, UnidadeCurricular, Tecnologia, Competencia, Projeto
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nome', 'titulo_profissional', 'link_linkedin')
    search_fields = ('nome', 'titulo_profissional')
    list_editable = ('titulo_profissional',)

admin.site.register(Perfil, PerfilAdmin)


class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ects_totais', 'perfil')
    search_fields = ('nome',)

admin.site.register(Licenciatura, LicenciaturaAdmin)

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'link_pagina_pessoal')
    search_fields = ('nome',)

admin.site.register(Docente, DocenteAdmin)

class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ects', 'ano_semestre')
    search_fields = ('nome',)
    list_filter = ('ano_semestre',)

admin.site.register(UnidadeCurricular, UnidadeCurricularAdmin)

class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nivel_interesse')
    search_fields = ('nome',)
    list_filter = ('nivel_interesse',)

admin.site.register(Tecnologia, TecnologiaAdmin)

class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'nivel_dominio')
    search_fields = ('nome', 'categoria')
    list_filter = ('categoria', 'nivel_dominio')

admin.site.register(Competencia, CompetenciaAdmin)

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'unidade_curricular', 'link_github')
    search_fields = ('nome', 'descricao')
    list_filter = ('unidade_curricular',)

admin.site.register(Projeto, ProjetoAdmin)