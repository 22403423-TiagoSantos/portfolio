from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .models import Artigo, Comentario
from .forms import ArtigoForm, ComentarioForm
from accounts.forms import RegistoForm

def registo_artigos(request):
    form = RegistoForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        grupo, created = Group.objects.get_or_create(name='autores')
        user.groups.add(grupo)
        return redirect('accounts:login')
    return render(request, 'artigos/registo.html', {'form': form})

def lista_artigos(request):
    artigos = Artigo.objects.all().order_by('-data_criacao') 
    return render(request, 'artigos/lista.html', {'artigos': artigos})

def detalhe_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    comentarios = artigo.comentarios.all().order_by('-data_criacao')
    form = ComentarioForm()

    if request.method == "POST" and request.user.is_authenticated:
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.artigo = artigo
            comentario.autor = request.user
            comentario.save()
            return redirect('artigos:detalhe', artigo_id=artigo.id)

    context = {'artigo': artigo, 'comentarios': comentarios, 'form': form}
    return render(request, 'artigos/detalhe.html', context)

@login_required
def novo_artigo(request):
    if not request.user.groups.filter(name='autores').exists():
        return redirect('artigos:lista')

    form = ArtigoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        artigo = form.save(commit=False)
        artigo.autor = request.user
        artigo.save()
        return redirect('artigos:lista')
    return render(request, 'artigos/novo_artigo.html', {'form': form})

@login_required
def edita_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    
    if not request.user.groups.filter(name='autores').exists() or request.user != artigo.autor:
        return redirect('artigos:lista')
    
    form = ArtigoForm(request.POST or None, request.FILES or None, instance=artigo)
    if form.is_valid():
        form.save()
        return redirect('artigos:detalhe', artigo_id=artigo.id)
    return render(request, 'artigos/edita_artigo.html', {'form': form, 'artigo': artigo})

@login_required
def like_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    if request.user in artigo.likes.all():
        artigo.likes.remove(request.user)
    else:
        artigo.likes.add(request.user)
    return redirect('artigos:detalhe', artigo_id=artigo.id)