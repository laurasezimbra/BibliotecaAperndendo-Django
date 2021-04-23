from django.shortcuts import render


def index(request):
    context = {
        'curso': 'Programação web com Djago Framework', 'Livraria': 'é uma boa pegada'
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')
