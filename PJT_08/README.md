# REST API



## 1. 장고 프로젝트를 시작한다.

## 2. Movie, Review, Genre 모델을 만든다

```python
from django.db import models
from django.conf import settings
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=20)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=20000)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='movies')

class Review(models.Model):
    content = models.CharField(max_length=100)
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')

```



## serializer.py 를 movies 앱에 만들고 직렬화를 하기위한 class 를 제작한다.

```python
from rest_framework import serializers
from .models import Movie, Review, Genre

class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = ('id', 'name', )

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'audience', 'poster_url', 'description', 'genre' )

class GenreDetailSerializer(GenreSerializer):
    movies = MovieSerializer(many=True) # 장르에 들어있는 movies를 상세보기로 보기위하여
    class Meta(GenreSerializer.Meta):
        fields = GenreSerializer.Meta.fields + ('movies', )
        

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'content', 'movie_id', 'user_id', 'score' )

class MovieDetailSerializer(MovieSerializer):
    reviews = ReviewSerializer
    class Meta(MovieSerializer.Meta):
        fields = MovieSerializer.Meta.fields + ('reviews', )


```



## 필요한 요청에따른 url과 views 함수를 만든다.



### List 를 불러오기 위한 함수.

```python
@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
```



### Detail을 불러오기 위한 함수

```python
@api_view(['GET'])
def genre_detail(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    serializer = GenreDetailSerializer(genre)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)
```



### reviews 작성, 삭제, 수정을 위한 함수

```python
@api_view(['POST'])
def create_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(movie_id=movie_pk, user_id=request.data['user_id'])
        # 현재 사용자를 받아오는 기능이 구현되어있지 않아 살짝 억지로 넣어준다. POST에서 보내줘야한다
    return Response(serializer.data)

@api_view(['DELETE', 'PUT', 'GET'])
def update_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'PUT':
        serializer = ReviewSerializer(data=request.data, instance=review)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response({'message': '삭제되었습니다'})
    else:
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
```

