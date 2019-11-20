from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Genre, Review
from .forms import CommentForm


# Create your views here.

def index(request):
    movies = Movie.objects.all()

    return render(request, 'movies/index.html', {'movies': movies})

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    comment_form = CommentForm()

    return render(request, 'movies/detail.html', {'movie': movie, 'comment_form': comment_form})


def create_review(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    form = CommentForm(request.POST)

    if form.is_valid():
        print('들어감')
        comment = form.save(commit=False)
        comment.movie_id = movie_id
        comment.user_id = request.user.id
        comment.save()
    
    return redirect('movies:detail', movie_id)

def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    movie_id = review.movie.id
    review.delete()

    return redirect('movies:detail', movie_id)

def like(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    user = request.user

    if movie.liked_users.filter(pk=user.id).exists():
        user.liked_movies.remove(movie)
    
    else:
        user.liked_movies.add(movie)
    
    return redirect('movies:detail', movie.id)