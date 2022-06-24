from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'receitas/home.html')


def contato(request):
    return HttpResponse('contato156')


def sobre(request):
    return HttpResponse('sobre-everyone')
