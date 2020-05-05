from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

class Index(View):
    model = 'Elogio'
    template_name = 'Elogio/index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return render(request, 'Elogio/login.html')


def login_index(request):
    if request.method != 'POST':
        return render(request, 'Elogio/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login_index')


def login(request):
    template_name = 'Elogio/index.html'
    if request.method != 'POST':
        return render(request, 'Elogio/login.html')
    if request.user.is_authenticated:
        return render(request, template_name)

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos.')
        return render(request, 'Elogio/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Você fez login com sucesso.')
        return redirect('index')