from django.http import HttpResponse
from django.shortcuts import render

from .models import Game


def main(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', {'games': games, })

def game_page(request, id):
    game = Game.objects.get(pk=id)
    return render(request, 'games/game_page.html', {'game': game, })
