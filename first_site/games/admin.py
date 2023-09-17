from django.contrib import admin
from .models import Game, Category, Profile, Complilation, Review
admin.site.register(Game)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Complilation)
admin.site.register(Review)