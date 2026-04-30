from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistoForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('pagina_inicial_do_portfolio')
        else:
            return render(request, 'accounts/login.html', {
                'mensagem': 'Credenciais inválidas'
            })
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def registo_view(request):
    form = RegistoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    context = {'form': form}
    return render(request, 'accounts/registo.html', context)

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail

def solicitar_link_magico(request):
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            link = f"http://{request.get_host()}/accounts/verify/{uid}/{token}/"
            
            send_mail(
                'Teu Link Mágico de Login',
                f'Clica aqui para entrar: {link}',
                'admin@teuportfolio.pt',
                [user.email],
            )
            return render(request, 'accounts/login.html', {'mensagem': 'Verifica o teu terminal (email)!'})
        except User.DoesNotExist:
            return render(request, 'accounts/login.html', {'mensagem': 'Email não encontrado'})
    return render(request, 'accounts/login_magico.html')

def verificar_link_magico(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        login(request, user)
        return redirect('portfolio:index')
    else:
        return render(request, 'accounts/login.html', {'mensagem': 'Link inválido ou expirado'})