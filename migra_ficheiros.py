import os
from django.core.files import File
from django.conf import settings

# Importa os modelos das apps
from portfolio.models import Perfil, UnidadeCurricular, Tecnologia, Projeto, Formacao, MakingOf
from artigos.models import Artigo
from escola.models import Curso

def migrar_objeto(obj, campo_imagem):
    """ Função auxiliar para migrar a imagem de um objeto para o Cloudinary """
    campo = getattr(obj, campo_imagem)
    if campo and campo.name:
        try:
            local_path = os.path.join(settings.MEDIA_ROOT, obj.imagem.name)
            if os.path.exists(local_path):
                with open(local_path, 'rb') as f:
                    campo.save(
                        os.path.basename(local_path),
                        File(f),
                        save=True
                    )
                print(f"✅ Sucesso [{obj.__class__.__name__}]: {obj}")
            else:
                print(f"⚠️ Ficheiro local não encontrado para: {obj}")
        except Exception as e:
            print(f"❌ Erro ao migrar {obj}: {e}")

# --- Execução da Migração ---

print("A iniciar migração para Cloudinary...")

# --- App: Portfolio ---
print("\n--> A migrar modelos do Portfolio...")
for obj in Perfil.objects.all():
    migrar_objeto(obj, 'foto_perfil')

for obj in UnidadeCurricular.objects.all():
    migrar_objeto(obj, 'imagem')

for obj in Tecnologia.objects.all():
    migrar_objeto(obj, 'logo')

for obj in Projeto.objects.all():
    migrar_objeto(obj, 'imagem')

for obj in Formacao.objects.all():
    migrar_objeto(obj, 'logotipo')

for obj in MakingOf.objects.all():
    migrar_objeto(obj, 'imagem')

# --- App: Artigos ---
print("\n--> A migrar modelos de Artigos...")
for obj in Artigo.objects.all():
    migrar_objeto(obj, 'fotografia')

# --- App: Escola ---
print("\n--> A migrar modelos de Escola...")
for obj in Curso.objects.all():
    migrar_objeto(obj, 'imagem')

print("\n🎉 Migração concluída com sucesso!")