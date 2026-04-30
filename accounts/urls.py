from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registo/', views.registo_view, name='registo'),
    path('login-magico/', views.solicitar_link_magico, name='solicitar_link'),
    path('validar/<uidb64>/<token>/', views.verificar_link_magico, name='validar_link'),
]