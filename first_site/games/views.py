from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from .forms import CommentForm
from .models import Game
from .services import get_all_games, add_categories, get_game, add_compilations, get_reviews, create_comment, \
    get_category_with_games, get_compilations_with_games


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
    comment_form = CommentForm()
    reviews = get_reviews(game)
    page_data = {'game': game, "comment_form": comment_form, "reviews": reviews}
    return render(request, 'games/game_page.html', page_data)

@login_required()
@require_http_methods(["POST"])
def add_comment(request, id):
    form = CommentForm(request.POST)
    if form.is_valid():
        create_comment(request.user, id, form.cleaned_data['comment_text'], form.cleaned_data['rating'])
    return redirect(reverse("game_page", kwargs={"id": id}))

def category_page(request, id):
    category, games = get_category_with_games(id)
    page_data = {"category": category, "games": games}
    add_categories(page_data)
    add_compilations(page_data)
    return render(request, 'games/index.html', page_data)

def compilations_page(request):
    page_data = {}
    add_categories(page_data)
    add_compilations(page_data)
    print(page_data)
    return render(request, 'compilations_page.html', page_data)

def compilation_page(request, id):
    compilation, games = get_compilations_with_games(id)
    page_data = {"compilation": compilation, "games": games}
    add_categories(page_data)
    add_compilations(page_data)
    return render(request, 'games/index.html', page_data)