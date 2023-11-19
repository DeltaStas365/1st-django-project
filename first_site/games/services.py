from .models import Game, Category, Complilation


def get_all_games():
    return Game.objects.all()

def add_categories(data):
    categories = Category.objects.all()
    data["categories"] = categories

def get_game(id):
    return Game.objects.get(pk=id)

def add_compilations(data):
    compilations = Complilation.objects.all()
    data["compilations"] = compilations