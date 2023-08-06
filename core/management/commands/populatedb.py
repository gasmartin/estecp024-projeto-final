import csv

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from core.models import Movie


FILE_PATH = settings.BASE_DIR / "core" / "data" / "movies.csv"


class Command(BaseCommand):
    help = "Read CSV file containing movies and populate database"

    def handle(self, *args, **options):
        with open(FILE_PATH) as file:
            for row in csv.reader(file, delimiter=","):
                movie = Movie()
                movie.poster_link = row[0]
                movie.title = row[1]
                movie.released_year = row[2]
                movie.genre = row[3]
                movie.overview = row[4]
                movie.director = row[5]
                movie.starring = ", ".join(row[6:])
                try:
                    movie.save()
                except Exception as e:
                    raise CommandError(f"Unable to save movie {movie.title}") from e
                self.stdout.write(self.style.SUCCESS(f"Successfully saved {movie.title}"))
        self.stdout.write(self.style.SUCCESS("Successfully populated database"))
