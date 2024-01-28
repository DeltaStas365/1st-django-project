from .models import Game, Category, Compilation, Review

def create_comment(author, game_id, text, rating):
    game = get_game(game_id)
    review = Review(author=author, game=game, text=text, rate=rating)
    review.save()
    game.reviews_count += 1
    game.rate = ((game.reviews_count - 1)*game.rate + rating) / game.reviews_count
    game.save()

def get_all_games():
    return Game.objects.all()

def add_categories(data):
    categories = Category.objects.all()
    data["categories"] = categories

def get_game(id):
    return Game.objects.get(pk=id)

def get_reviews(game: Game):
    return game.reviews.all()

def add_compilations(data):
    compilations = Compilation.objects.all()
    data["compilations"] = compilations

def get_category_with_games(id):
    category = Category.objects.get(pk=id)
    games = category.games.all()
    return category, games

def get_compilations_with_games(id):
    compilation = Compilation.objects.get(pk=id)
    games = compilation.game.all()
    return compilation, games