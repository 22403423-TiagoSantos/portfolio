from django.shortcuts import render
from .models import Projeto, Tecnologia, Competencia, TFC, UnidadeCurricular, Formacao, MakingOf, Licenciatura, Docente, Perfil

def index(request):
    perfil = Perfil.objects.first() 
    context = {'perfil': perfil}
    return render(request, 'portfolio/index.html', context)

def projetos_view(request):
    projetos = Projeto.objects.all()
    context = {'projetos': projetos}
    return render(request, 'portfolio/projetos.html', context)

def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    context = {'tecnologias': tecnologias}
    return render(request, 'portfolio/tecnologias.html', context)

def tfcs_view(request):
    tfcs = TFC.objects.all()
    context = {'tfcs': tfcs}
    return render(request, 'portfolio/tfcs.html', context)

def competencias_view(request):
    competencias = Competencia.objects.all()
    context = {'competencias': competencias,}
    return render(request, 'portfolio/competencias.html', context)

def ucs_view(request):
    ucs = UnidadeCurricular.objects.all().order_by('ano', 'semestre')
    context = {'ucs': ucs,}
    return render(request, 'portfolio/ucs.html', context)

def formacoes_view(request):
    formacoes = Formacao.objects.all().order_by('-data_conclusao')
    context = {'formacoes': formacoes,}
    return render(request, 'portfolio/formacoes.html', context)

def makingof_view(request):
    makingofs = MakingOf.objects.all()
    context = {'makingofs': makingofs,}
    return render(request, 'portfolio/makingof.html', context)

def licenciaturas_view(request):
    licenciaturas = Licenciatura.objects.all()
    return render(request, 'portfolio/licenciaturas.html', {'licenciaturas': licenciaturas})

def docentes_view(request):
    docentes = Docente.objects.all()
    return render(request, 'portfolio/docentes.html', {'docentes': docentes})