from django.http import HttpResponse
from django.db import connection
from .models import Movies

def init(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ex02_movies (
                    episode_nb SERIAL PRIMARY KEY,
                    title VARCHAR(64) NOT NULL UNIQUE,
                    opening_crawl TEXT,
                    director VARCHAR(32) NOT NULL,
                    producer VARCHAR(128) NOT NULL,
                    release_date DATE NOT NULL
                );
            """)
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")


def populate(request):
    try:
        
		# Delete existing data
        Movies.objects.all().delete()

        movie_data = [
            {
                'episode_nb': 1,
                'title': 'The Phantom Menace',
                'director': 'George Lucas',
                'producer': 'Rick McCallum',
                'release_date': '1999-05-19'
            },
            {
                'episode_nb': 2,
                'title': 'Attack of the Clones',
                'director': 'George Lucas',
                'producer': 'Rick McCallum',
                'release_date': '2002-05-16'
            },
            {
                'episode_nb': 3,
                'title': 'Revenge of the Sith',
                'director': 'George Lucas',
                'producer': 'Rick McCallum',
                'release_date': '2005-05-19'
            },
            {
                'episode_nb': 4,
                'title': 'A New Hope',
                'director': 'George Lucas',
                'producer': 'Gary Kurtz, Rick McCallum',
                'release_date': '1977-05-25'
            },
            {
                'episode_nb': 5,
                'title': 'The Empire Strikes Back',
                'director': 'Irvin Kershner',
                'producer': 'Gary Kurtz, Rick McCallum',
                'release_date': '1980-05-17'
            },
            {
                'episode_nb': 6,
                'title': 'Return of the Jedi',
                'director': 'Richard Marquand',
                'producer': 'Howard G. Kazanjian, George Lucas, Rick McCallum',
                'release_date': '1983-05-25'
            },
            {
                'episode_nb': 7,
                'title': 'The Force Awakens',
                'director': 'J. J. Abrams',
                'producer': 'Kathleen Kennedy, J. J. Abrams, Bryan Burk',
                'release_date': '2015-12-11'
            }
        ]
        
        response_text = ""
        for data in movie_data:
            Movies.objects.create(**data)
            response_text += "OK\n"
        
        return HttpResponse(response_text)
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")

from django.http import HttpResponse
from .models import Movies

def display(request):
    try:
        # Retrieve all movies from the database
        movies = Movies.objects.all()
        
        # If there are no movies available, display "No data available"
        if not movies:
            return HttpResponse("No data available")
        
        # Prepare HTML content for displaying movies in a table
        html_content = "<table border='1'><tr><th>Title</th><th>Episode Number</th><th>Director</th><th>Producer</th><th>Release Date</th></tr>"
        for movie in movies:
            html_content += f"<tr><td>{movie.title}</td><td>{movie.episode_nb}</td><td>{movie.director}</td><td>{movie.producer}</td><td>{movie.release_date}</td></tr>"
        html_content += "</table>"
        
        return HttpResponse(html_content)
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")
