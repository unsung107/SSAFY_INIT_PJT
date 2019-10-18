from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment, Movie
from .forms import MovieForm, CommentForm
# Create your views here.

def index(request):
    movies = Movie.objects.all()
    print(movies)
    return render(request, 'movies/index.html', {'movies': movies})

def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')

    else:
        form = MovieForm()
    
    return render(request, 'movies/create.html', {'form': form})

def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comments = movie.comments.all()
    comment_form = CommentForm
    context = {'movie':movie, 'comments':comments, 'comment_form':comment_form}
    return render(request, 'movies/detail.html', context)

def delete(request, movie_pk):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_pk)
        movie.delete()
    return redirect('movies:index')

def update(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)

        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie_pk)
    else:
        form = MovieForm(instance=movie)
    
    return render(request, 'movies/update.html', {'form': form, 'movie':movie})

def comment_create(request, movie_pk):
    # movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie_id = movie_pk
            comment.save()
        return redirect('movies:detail', movie_pk)

    return render(request, 'movies/detail.html', {'form': form})
    