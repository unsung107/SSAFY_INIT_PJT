from django.contrib import admin
from .models import Movie
# Register your models here.

@admin.register(Movie)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'title_en')

