from django.contrib import admin
from .models import Perfil

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nome', 'titulo_profissional', 'link_linkedin')
    search_fields = ('nome', 'titulo_profissional')
    list_editable = ('titulo_profissional',)

admin.site.register(Perfil, PerfilAdmin)