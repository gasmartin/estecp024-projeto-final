import uuid

from django.db import models


# Create your models here.
class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
