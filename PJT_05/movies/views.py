from django.shortcuts import render
from .models import Movie

# Create your views here.

def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies
    }

    return render(request, 'movies/index.html', context)

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie': movie
    }

    return render(request, 'movies/detail.html', context)

def new(request):
    return render(request, 'movies/new.html')

def create(request):
    title = request.GET.get('title')
    title_en = request.GET.get('title_en')
    audience = request.GET.get('audience')
    open_date = request.GET.get('open_date')
    genre = request.GET.get('genre')
    watch_grade = request.GET.get('watch_grade')
    score = request.GET.get('score')
    poster_url = request.GET.get('poster_url')
    description = request.GET.get('description')
    movie = Movie(title=title, title_en=title_en, audience=audience, open_date=open_date, genre=genre, watch_grade=watch_grade, score=score, poster_url=poster_url, description=description)
    movie.save()


    context = {
        'title': movie.title
    }

    return render(request, 'movies/create.html', context)

def edit(request, edit_pk):
    context = {
        'edit_pk': edit_pk
    }

    return render(request, 'movies/edit.html', context)

def update(request, edit_pk):
    movie = Movie.objects.get(pk=edit_pk)

    movie.title = request.GET.get('title')
    movie.title_en = request.GET.get('title_en')
    movie.audience = request.GET.get('audience')
    movie.open_date = request.GET.get('open_date')
    movie.genre = request.GET.get('genre')
    movie.watch_grade = request.GET.get('watch_grade')
    movie.score = request.GET.get('score')
    movie.poster_url = request.GET.get('poster_url')
    movie.description = request.GET.get('description')

    movie.save()

    context = {
        'title': movie.title
    }

    return render(request, 'movies/update.html', context)


def delete(request, delete_pk):
    movie = Movie.objects.get(pk=delete_pk)
    title = movie.title
    context = {
        'title': title,
    }
    movie.delete()
    return render(request, 'movies/delete.html', context)

