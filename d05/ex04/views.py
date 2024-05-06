from django.http import HttpResponse
import psycopg2
from psycopg2 import sql

def init(request):
    conn = None
    try:
        conn = psycopg2.connect(
            dbname="djangotraining",
            user="djangouser",
            password="secret",
            host="localhost"
        )
        cur = conn.cursor()
        cur.execute(
            sql.SQL("""CREATE TABLE IF NOT EXISTS ex00_movies (
                title VARCHAR(64) NOT NULL UNIQUE,
                episode_nb SERIAL PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
            );""")
        )
        conn.commit()
        cur.close()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}", status=500)
    finally:
        if conn is not None:
            conn.close()

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
    
def display(request):
    try:
        # Retrieve all movies from the database
        movies = Movies.objects.all()
        
        # If there are no movies available, display "No data available"
        if not movies:
            return HttpResponse("No data available")
        
        html_content = "<table border='1'><tr><th>Title</th><th>Episode Number</th><th>Director</th><th>Producer</th><th>Release Date</th></tr>"
        for movie in movies:
            html_content += f"<tr><td>{movie.title}</td><td>{movie.episode_nb}</td><td>{movie.director}</td><td>{movie.producer}</td><td>{movie.release_date}</td></tr>"
        html_content += "</table>"
        
        return HttpResponse(html_content)
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")

from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies

def remove(request):
    if request.method == 'POST':
        # Get the selected film title from the form
        selected_title = request.POST.get('film_title')

        # Check if a film title is selected
        if selected_title:
            try:
                # Query the database for the movie with the selected title
                movie = Movies.objects.get(title=selected_title)
                
                # Delete the movie from the database
                movie.delete()
                
                # Fetch the remaining movie titles from the database
                movie_titles = Movies.objects.values_list('title', flat=True)
                
                # Render the form with the updated list of movie titles
                return render(request, 'ex04/remove.html', {'movie_titles': movie_titles})
            except Movies.DoesNotExist:
                # Handle the case where the selected movie does not exist
                return HttpResponse("Selected movie does not exist.")
            except Exception as e:
                # Handle other exceptions
                return HttpResponse(f"An error occurred: {e}")
        else:
            # Handle the case where no film title is selected
            return HttpResponse("No film title selected.")
    else:
        try:
            # Fetch all movie titles from the database
            movie_titles = Movies.objects.values_list('title', flat=True)
            
            # Render the form with the list of movie titles
            return render(request, 'ex04/remove.html', {'movie_titles': movie_titles})
        except Exception as e:
            # Handle exceptions
            return HttpResponse(f"An error occurred: {e}")
