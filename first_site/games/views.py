from django.http import HttpResponse
from django.shortcuts import render

from .models import Game
from .services import get_all_games, add_categories, get_game, add_compilations


def main(request):
    games = get_all_games()
    search_query = request.GET.get("q", None)
    if search_query:
        games = Game.objects.filter(name__icontains=search_query)
        page_data = {'games': games, }
        add_categories(page_data)
        add_compilations(page_data)
    else:
        page_data = {'games': games, }
        add_categories(page_data)
        add_compilations(page_data)
    return render(request, 'games/index.html', page_data)

def game_page(request, id):
    game = get_game(id)
    return render(request, 'games/game_page.html', {'game': game, })
