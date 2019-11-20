from django.contrib import admin
from .models import Movie, Review, Genre
# Register your models here.

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Review)