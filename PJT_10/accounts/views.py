from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
User = get_user_model()
# Create your views here.

def index(request):
    users = User.objects.all()
    print(users)
    context = {'users': users}
    return render(request,'accounts/index.html', context)

def signup(request):
    # if request.user.is_authenticated:
    #     return redirect('accounts:index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            next_page = request.GET.get('index')
            return redirect(next_page or 'accounts:index')
    
    else:
        form = CustomUserCreationForm()
    
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

def detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    reviews = user.reviews.all()
    movies = user.liked_movies.all()
    
    context = {
        'user': user,
        'reviews': reviews,
        'movies': movies,
    }
    return render(request, 'accounts/detail.html', context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_page = request.GET.get('next')
            return redirect(next_page or 'accounts:index')

    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form' : form})

def logout(reqeust):
    auth_logout(reqeust)
    return redirect('accounts:index')