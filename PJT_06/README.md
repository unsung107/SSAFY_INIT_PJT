# PJT 06

## 프레임워크 기반 웹 페이지 구현

### 1. 데이터베이스에 movie와 comment를 넣기위하여 모델을 작성한다

`moives/models.py`

```python
from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    title_en = models.CharField(max_length=20)
    audience = models.IntegerField()
    open_date = models.DateField()
    genre = models.CharField(max_length=20)
    watch_grade = models.CharField(max_length=20)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()

    class Meta:
        ordering = ('-pk', )

class Comment(models.Model):
    content = models.CharField(max_length=20)
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ('-pk', )
```

### 2. 필요한 페이지들을 movies/urls.py 에 넣어놓는다

`movies/urls.py`

```python
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/update/', views.update, name='update'),
    path('<int:movie_pk>/delete/', views.delete, name='delete'),
    path('<int:movie_pk>/reviews/', views.comment_create, name='comment_create'),
]

```

### 3. modelform 을 사용하기위하여 movies/forms.py 를 생성한다

`movies/forms.py`

```python
from django import forms
from .models import Movie, Comment


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = '__all__'

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content', 'score', )
        # exclude = ('article', )
```

### 4. 영화정보를 생성하기위한 view함수를 작성한다

`movies/views.py`

```python
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')

    else:
        form = MovieForm()
    
    return render(request, 'movies/create.html', {'form': form
```

post 요청으로 들어올시 생성

get 요청으로 들어오거나 form 이 잘못됐을 경우 생성페이지를 보여준다



### 5. 정보조회 페이지를 생성하기위하여 view함수를 작성한다

`movies/views.py`

```python
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comments = movie.comments.all()
    comment_form = CommentForm
    context = {'movie':movie, 'comments':comments, 'comment_form':comment_form}
    return render(request, 'movies/detail.html', context)
```

movie 변수에 원하는 영화를 선택하고 해당하는 영화에 있는 모든 댓글을 불러온후 

댓글을 작성할 form 과함께 render해준다



### 6. 수정과 삭제를 만든다

`movies/views.py`

```python
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
```

둘모두 post요청으로 올시 생성 및 수정

get요청으로 오거나 form 이 작성됐을시 redirect를 해준다

### 7. 영화정보 댓글만들기

`movies/views.py`

```python
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
```

위와 마찬가지로 작성한다.



끝!