from django.http import HttpResponse
from django.shortcuts import render

from .models import Game
from .services import get_all_games, add_categories


def main(request):
    games = get_all_games()
    page_data = {'games': games, }
    add_categories(page_data)
    return render(request, 'games/index.html', page_data)

def game_page(request, id):
    game = Game.objects.get(pk=id)
    return render(request, 'games/game_page.html', {'game': game, })
