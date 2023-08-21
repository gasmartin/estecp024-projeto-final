from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from .models import Movie, Review


# Create your views here.
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']

        if password != confirm_password:
            messages.error(request, 'Password does not match')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('register')

        user = User.objects.create_user(
            username=username, 
            password=password, 
            email=email,
            first_name=first_name, 
            last_name=last_name
        )

        user.save()

        messages.success(
            request, 
            'Your user account has been created successfully. Now you can log-in'
        )
    
        return redirect('login')
    else:
        return render(request, 'registration/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(
                request, 
                'Invalid username or password. Please try again.'
            )
            return redirect('login')
    else:
        return render(request, 'registration/login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


def search(request):
    if request.method == 'GET':
        try:
            q = request.GET['q']
        except MultiValueDictKeyError:
            return redirect('home')

        movies = Movie.objects.filter(title__icontains=q)

        context = {
            'movies': movies,
            'q': q,
        }

        return render(request, 'search_result.html', context)
    else:
        return redirect('home')


def movie(request, movie_id):
    if request.method == 'GET': 
        movie = Movie.objects.get(id=movie_id)
        reviews = Review.objects.filter(movie=movie)

        context = {
            'movie': movie,
            'reviews': reviews,
        }

        if request.user.is_authenticated:
            context['user_review'] = Review.objects.filter(
                movie=movie, 
                user=request.user
            ).first()

        return render(request, 'movie_details.html', context)
    else:
        return redirect('home')


@login_required
def review(request, movie_id):
    pass
