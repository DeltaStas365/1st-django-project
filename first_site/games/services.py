from .models import Game, Category


def get_all_games():
    return Game.objects.all()

def add_categories(data):
    categories = Category.objects.all()
    data["categories"] = categories