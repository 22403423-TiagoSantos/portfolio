from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('', views.lista_artigos, name='lista'),
    path('<int:artigo_id>/', views.detalhe_artigo, name='detalhe'),
    path('novo/', views.novo_artigo, name='novo'),
    path('<int:artigo_id>/editar/', views.edita_artigo, name='editar'),
    path('<int:artigo_id>/like/', views.like_artigo, name='like'),
    path('registo/', views.registo_artigos, name='registo'),
]