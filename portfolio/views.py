from django.shortcuts import render, redirect
from .models import Projeto, Tecnologia, Competencia, TFC, UnidadeCurricular, Formacao, MakingOf, Licenciatura, Docente, Perfil, TipoTecnologia
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm
from django.contrib.auth.decorators import login_required

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

@login_required
def novo_projeto_view(request):
    form = ProjetoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:projetos')
    
    context = {'form': form}
    return render(request, 'portfolio/novo_projeto.html', context)

@login_required
def edita_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    form = ProjetoForm(request.POST or None, request.FILES or None, instance=projeto)
    
    if form.is_valid():
        form.save()
        return redirect('portfolio:projetos')
        
    context = {'form': form, 'projeto': projeto}
    return render(request, 'portfolio/edita_projeto.html', context)

@login_required
def apaga_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    projeto.delete()
    return redirect('portfolio:projetos')

@login_required
def nova_tecnologia_view(request):
    form = TecnologiaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:tecnologias')
    
    context = {'form': form}
    return render(request, 'portfolio/nova_tecnologia.html', context)

@login_required
def edita_tecnologia_view(request, tecnologia_id):
    tecnologia = Tecnologia.objects.get(id=tecnologia_id)
    form = TecnologiaForm(request.POST or None, request.FILES or None, instance=tecnologia)
    
    if form.is_valid():
        form.save()
        return redirect('portfolio:tecnologias')
        
    context = {'form': form, 'tecnologia': tecnologia}
    return render(request, 'portfolio/edita_tecnologia.html', context)

@login_required
def apaga_tecnologia_view(request, tecnologia_id):
    tecnologia = Tecnologia.objects.get(id=tecnologia_id)
    tecnologia.delete()
    return redirect('portfolio:tecnologias')

@login_required
def nova_competencia_view(request):
    form = CompetenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:competencias')
    
    context = {'form': form}
    return render(request, 'portfolio/nova_competencia.html', context)

@login_required
def edita_competencia_view(request, competencia_id):
    competencia = Competencia.objects.get(id=competencia_id)
    form = CompetenciaForm(request.POST or None, instance=competencia)
    
    if form.is_valid():
        form.save()
        return redirect('portfolio:competencias')
        
    context = {'form': form, 'competencia': competencia}
    return render(request, 'portfolio/edita_competencia.html', context)

@login_required
def apaga_competencia_view(request, competencia_id):
    competencia = Competencia.objects.get(id=competencia_id)
    competencia.delete()
    return redirect('portfolio:competencias')

@login_required
def nova_formacao_view(request):
    form = FormacaoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:formacoes')
    
    context = {'form': form}
    return render(request, 'portfolio/nova_formacao.html', context)

@login_required
def edita_formacao_view(request, formacao_id):
    formacao = Formacao.objects.get(id=formacao_id)
    form = FormacaoForm(request.POST or None, request.FILES or None, instance=formacao)
    
    if form.is_valid():
        form.save()
        return redirect('portfolio:formacoes')
        
    context = {'form': form, 'formacao': formacao}
    return render(request, 'portfolio/edita_formacao.html', context)

@login_required
def apaga_formacao_view(request, formacao_id):
    formacao = Formacao.objects.get(id=formacao_id)
    formacao.delete()
    return redirect('portfolio:formacoes')

def sobre_view(request):
    tipos = TipoTecnologia.objects.all()
    
    texto_making_of = """
### O Desafio
O objetivo deste projeto da cadeira de Programação Web é construir um **Portfólio Dinâmico** utilizando a framework *Django*.

Ao longo do desenvolvimento, aprendemos a:
* Implementar a arquitetura MVT (Model-View-Template).
* Criar operações CRUD completas.
* Gerir bases de dados relacionais e ficheiros estáticos/media.
    """
    
    context = {
    'tipos': tipos,
    'texto_exemplo_makingof': texto_making_of
}
    
    return render(request, 'portfolio/sobre.html', context)