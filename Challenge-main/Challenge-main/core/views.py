from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import ClienteForm
from .models import AcervoVideos


def index(request):
    return render(request, 'core/index.html')

def admin(request):
    return render(request, 'core/portal_admin.html')

def cadastro_geral(request):
    return render(request, 'core/cadastro_geral.html')

def acervo_videos(request):
    lista_videos = [
        'https://www.youtube.com/watch?v=BPnaXaEq_Hg&list=PLONqVfazBqhWMeuAmfn-5znJ1tamV8jGc&index=2',
        'https://www.youtube.com/watch?v=fFuTkavmsxo&list=PLONqVfazBqhWMeuAmfn-5znJ1tamV8jGc&index=3',
        'https://www.youtube.com/watch?v=AGdSBSVMYR8&list=PLONqVfazBqhWMeuAmfn-5znJ1tamV8jGc&index=4',
        'https://www.youtube.com/watch?v=ffGd7biISFg&list=PLONqVfazBqhWMeuAmfn-5znJ1tamV8jGc&index=5',
        'https://www.youtube.com/watch?v=JU823WoH3W8',
        'https://www.youtube.com/watch?v=PI3GopnvQ54',
        'https://www.youtube.com/watch?v=Ie4S6Qxi6do'
    ]

    context = {
        'videos': lista_videos,
    }

    return render(request, 'core/acervo_videos.html', context)


def login(request):
    return render(request, 'login.html')

def cadastro_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../login')
    else:
        form = ClienteForm()

    return render(request, "core/cadastro_cliente.html", {'form': form})

def login_pagina(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('../index')
        else:
            return render(request, 'core/login.html', {'error': 'Login inválido.'})
    else:
        return render(request, 'core/login.html')


def ger_treinamento(request):
    acervo_videos = AcervoVideos.objects.all()
    return render(request, 'ger_treinamento.html', {'acervo_videos': acervo_videos})
