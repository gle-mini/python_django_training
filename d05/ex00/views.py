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

