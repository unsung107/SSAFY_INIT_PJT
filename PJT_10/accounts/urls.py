from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('<int:user_id>/', views.detail, name='detail'),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]
