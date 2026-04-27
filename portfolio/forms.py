from django import forms
from .models import Projeto, Tecnologia, Competencia, Formacao

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'
        
        labels = {
            'nome': 'Nome do Projeto',
            'ano_realizacao': 'Ano de Realização',
            'conceitos_aplicados': 'Conceitos Aplicados',
            'unidade_curricular': 'Disciplina (Opcional)',
        }

class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = '__all__'

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = '__all__'

class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = '__all__'
        
        widgets = {
            'data_conclusao': forms.DateInput(attrs={'type': 'date'}),
        }