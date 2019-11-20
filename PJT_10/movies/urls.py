from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:movie_id>/', views.detail, name='detail'),
    path('<int:movie_id>/review/', views.create_review, name='create_review'),
    path('<int:review_id>/delete_review/', views.delete_review, name='delete_review'),
    path('<int:movie_id>/like/', views.like, name="like"),

]
