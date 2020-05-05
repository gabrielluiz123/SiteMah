from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .models import Elogio
from .forms import FormElogio
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

class PostDetalhes(View):
    template_name = 'Elogio/comentario.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.contexto = {
            'comentarios': Elogio.objects.all().order_by('-data_comentario'),
            'form': FormElogio(request.POST or None),
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)

    def post(self, request, *args, **kwargs):
        form = self.contexto['form']
        if not form.is_valid():
            return render(request, self.template_name, self.contexto)
        comentario = form.save(commit=False)

        if request.user.is_authenticated:
            comentario.usuario_comentario = request.user
        comentario.save()
        messages.success(self.request, 'Comentario Adicionado com sucesso!!')

        return redirect('post_detalhes')


class Index(View):
    model = 'Elogio'
    template_name = 'Elogio/index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return render(request, 'Elogio/login.html')


def login_index(request):
    template_name = 'Elogio/index.html'
    if request.user.is_authenticated:
        return render(request, template_name)
    if request.method != 'POST':
        return render(request, 'Elogio/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login_index')


def login(request):
    template_name = 'Elogio/index.html'
    if request.user.is_authenticated:
        return render(request, template_name)
    if request.method != 'POST':
        return render(request, 'Elogio/login.html')


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