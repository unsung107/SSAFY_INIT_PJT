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