import os
import json
from portfolio.models import UnidadeCurricular, Licenciatura

UnidadeCurricular.objects.all().delete()

pasta_files = 'files'

licenciatura_lei = Licenciatura.objects.filter(nome__icontains="Engenharia Informática").first()

for filename in os.listdir(pasta_files):
    
    if filename.endswith('-PT.json'):
        filepath = os.path.join(pasta_files, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            if 'curricularUnitName' in data:
                
                uc = UnidadeCurricular.objects.create(
                    codigo = data.get('curricularIUnitReadableCode', ''),
                    nome = data.get('curricularUnitName', 'Sem Nome'),
                    ano = data.get('curricularYear', 1),
                    ects = data.get('ects', 0),
                    objetivos = data.get('objectives', ''),
                    conteudos = data.get('programme', ''),
                    bibliografia = data.get('bibliography', ''),
                    metodologia = data.get('methodology', ''),
                    semestre = 1 
                )
                
    
                if licenciatura_lei:
                    uc.licenciaturas.add(licenciatura_lei)
                