from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster_link = models.CharField(max_length=1000)
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    starring = models.CharField(max_length=100)
    overview = models.TextField()
    runtime = models.CharField(max_length=10)
    released_year = models.CharField(max_length=4)

    def __str__(self):
        return self.title


class Review(models.Model):
    overall_rating = models.IntegerField()
    review_text = models.TextField()

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
