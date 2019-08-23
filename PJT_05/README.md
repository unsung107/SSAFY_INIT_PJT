# PJT_05

## 프로젝트 생성

```bash
$ venv

$ python -m venv venv

$ pip install django

```

를 입력하여 프로젝트 생성준비를 마친뒤

```bash
django-admin startproject PJT_05 .

python manage.py startapp movies
```

를 통해 프로젝트와 그 아래 어플리케이션을 설치한다.

그 후 기본적인 셋팅을 실시한다.







## 영화 정보 데이터 베이스 만들기

pjt_05 프로젝트에 존재하는 models.py 에서

```python
from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    title_en = models.CharField(max_length=20)
    audience = models.IntegerField()
    open_date = models.DateField()
    genre = models.CharField(max_length=10)
    watch_grade = models.CharField(max_length=10)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f'{self.title} - {self.score}'
```

을 사용하여 우리가 원하는 데이터 베이스 양식을 만든다.



```bash
$ python manage.py makemigrations

$ python manage.py migrate
```

를 이용하여 데이터 베이스를 적용시켜주고 예시 데이터를 만들어준다.

PJT_05에 존재하는

urls.py 에서

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('movies/', include('movies.urls')),
    path('admin/', admin.site.urls),
]

```

으로 작성하여 앞으로 movies/ 로 들어오는 주소를 movies 어플로 넘겨준다.

movies/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('<int:delete_pk>/delete/', views.delete),
    path('<int:edit_pk>/update/', views.update),
    path('<int:edit_pk>/edit/', views.edit),
    path('create/', views.create),
    path('new/', views.new),
    path('', views.index),
    path('<int:movie_pk>/', views.detail)
]
```

위와 같이 movies/ 를 통해 들어올 url 들을 urls.py에 등록해준다.



# 영화 생성 수정 삭제하기

아래과정에서는 생성시 만들어지는 id값을 url에 넣어주어 각 영화의 정보를 불러온뒤 수정 혹은 삭제한다.

영화의 정보를 불러오는 것은

```python
movie = Movie.objects.get(pk=movie_pk)
```

을 이용한다.



## 영화 생성하기

movies/new.html

```html
{% extends 'base.html' %}

{% block title %}영화 생성하기{% endblock title %}
{% block content %}
<h1>영화 생성하기</h1>
<form action="/movies/create/">
영화 제목 : <input type="text" name="title"><br>
영화 제목(영문) : <input type="text" name="title_en"><br>
누적관객수 : <input type="number" name="audience" id=""><br>
영화 개봉일: <input type="date" name="open_date"><br>
장르 : <input type="text" name="genre"><br>
관람등급 : <input type="text" name="watch_grade"><br>
평점 : <input type="number" name="score"><br>
포스터 URL : <input type="text" name="poster_url"><br>
영화상세정보 : <textarea name="description"></textarea><br>
<button type="submit">생성하기</button>
</form>
<hr>
<a href="/movies/"><button> 돌아가기 </button></a>
{% endblock content %}

```

과 같이 인풋값을 받아 create 로 보낸다.

views.create

```python
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
```

위와 같이 받은 정보를 저장해주고 새로운 Movie 의 객체를 생성하여 저장한다.

## 영화 수정하기

movies/edit.html

```html
{% extends 'base.html' %}
{% block title %}영화 수정하기{% endblock title %}
{% block content %}
<h1>영화 수정하기</h1>

<form action="/movies/{{ edit_pk }}/update/">
영화 제목 : <input type="text" name="title"><br>
영화 제목(영문) : <input type="text" name="title_en"><br>
누적관객수 : <input type="number" name="audience" id=""><br>
영화 개봉일: <input type="date" name="open_date"><br>
장르 : <input type="text" name="genre"><br>
관람등급 : <input type="text" name="watch_grade"><br>
평점 : <input type="number" name="score"><br>
포스터 URL : <input type="text" name="poster_url"><br>
영화상세정보 : <textarea name="description"></textarea><br>
<button type="submit">수정하기</button>
</form>

<hr>
<a href="/movies/"><button> 돌아가기 </button></a>
{% endblock content %}
```

으로 update url로 보내준뒤

views.update

```python
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
```

으로 수정해준다.



## 영화삭제하기

urls.py

```python
path('<int:delete_pk>/delete/', views.delete),
```

와 같이 url을 통해 삭제할 영화의 id값을 받아 온뒤



views.delete

```python
def delete(request, delete_pk):
    movie = Movie.objects.get(pk=delete_pk)
    title = movie.title
    context = {
        'title': title,
    }
    movie.delete()
    return render(request, 'movies/delete.html', context)

```

을 이용하여 삭제하여준다.