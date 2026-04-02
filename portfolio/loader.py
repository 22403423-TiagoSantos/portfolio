from portfolio.models import TFC, Licenciatura
import json

TFC.objects.all().delete()

with open('data/tfcs_deisi.json') as f:
    tfcs = json.load(f)

    for item in tfcs:

        partes = item['licenciatura'].split('.')
        
        nome_lic = partes[0].strip().replace("Licenciatura em ", "")
        
        ano_json = int(partes[-1].strip())

        licenciatura_obj = Licenciatura.objects.get(nome=nome_lic)

        TFC.objects.create(
            nome = item['titulo'],
            autor = item['autores'],
            orientador = item['orientadores'],
            sumario = item['resumo'],
            classificacao = item['rating'],
            licenciatura = licenciatura_obj,
            ano = ano_json,
            link_pdf = item['link_pdf'],
            link_imagem = item['link_imagem'],
            palavras_chave = item['palavras_chave']
        )