from django.contrib import admin
from .models import Game, Category, Profile, Review, Compilation

admin.site.register(Game)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Compilation)
admin.site.register(Review)