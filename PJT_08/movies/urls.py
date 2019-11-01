from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('genres/', views.genre_list, name='genre_list'),
    path('genres/<int:genre_pk>/', views.genre_detail, name='genre_detail'),
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('movies/<int:movie_pk>/reviews/', views.create_review, name='create_review'),
    path('reviews/<int:review_pk>/', views.update_review, name='update_review'),
    
]
