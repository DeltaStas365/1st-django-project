from django.http import HttpResponse
from django.shortcuts import render

from .models import Game


def main(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', {'games': games, })
