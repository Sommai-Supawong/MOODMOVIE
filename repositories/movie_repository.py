from sqlalchemy import select, func, or_
from models import Movie, Mood, Genre


class MovieRepository:
    """All catalog queries live here and return detached, usable domain objects."""

    def __init__(self, database):
        self._database = database

    def _movies(self, statement):
        with self._database.connect() as session:
            return list(session.scalars(statement.order_by(Movie.title)))

    def find_all(self):
        return self._movies(select(Movie))

    def find_by_id(self, movie_id):
        with self._database.connect() as session:
            return session.get(Movie, movie_id)

    def find_by_mood(self, mood):
        return self._movies(select(Movie).join(Movie.mood).where(func.lower(Mood.name) == mood.lower()))

    def find_by_genre(self, genre):
        return self._movies(select(Movie).join(Movie.genre).where(func.lower(Genre.name) == genre.lower()))

    def search(self, keyword):
        # autoescape treats SQL wildcard characters as literal user input.
        return self._movies(select(Movie).where(or_(
            func.lower(Movie.title).contains(keyword.lower(), autoescape=True),
            func.lower(Movie.description).contains(keyword.lower(), autoescape=True),
        )))

    def get_moods(self):
        with self._database.connect() as session:
            return list(session.scalars(select(Mood).order_by(Mood.id)))

    def get_genres(self):
        with self._database.connect() as session:
            return list(session.scalars(select(Genre).order_by(Genre.name)))
