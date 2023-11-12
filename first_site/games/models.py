from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatar', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=16, unique=True)
    desc = models.TextField(blank=True, null=True)
    min_price = models.IntegerField()
    max_price = models.IntegerField()
    preview_image = models.ImageField(upload_to='games_previews', blank=True, null=True)
    reviews_count = models.IntegerField(default=0)
    rate = models.DecimalField(default=0, max_digits=2, decimal_places=1)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    rate = models.IntegerField()
    text = models.TextField()


class Complilation(models.Model):
    game = models.ManyToManyField(Game, related_name="Compilation")
    name = models.CharField(max_length=32)
    desc_comp = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='comp_img', blank=True, null=True)

    def __str__(self):
        return self.name