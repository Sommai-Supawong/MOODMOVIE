from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Shared SQLAlchemy mapping behavior."""


from models.mood import Mood
from models.genre import Genre
from models.movie import Movie

__all__ = ["Base", "Mood", "Genre", "Movie"]
