import pytest
from sqlalchemy import select, func, text
from sqlalchemy.exc import IntegrityError
from models import Movie, Mood, Genre
from repositories.movie_repository import MovieRepository


def test_seed_idempotent_and_relational(app):
    database = app.extensions["database"]
    database.initialize()
    with database.connect() as session:
        assert session.scalar(select(func.count()).select_from(Movie)) == 24
        assert session.scalar(select(func.count()).select_from(Mood)) == 6
        assert session.scalar(select(func.count()).select_from(Genre)) == 8
        assert session.execute(text("PRAGMA foreign_keys")).scalar() == 1


def test_repository_filters_and_detached_relationships(app):
    repository = MovieRepository(app.extensions["database"])
    assert len(repository.find_all()) == 24
    assert repository.find_by_id(999) is None
    assert [m.title for m in repository.search("wormhole")] == ["Interstellar"]
    assert len(repository.find_by_mood("happy")) == 4
    assert all(m.genre.name == "Sci-Fi" for m in repository.find_by_genre("sci-fi"))
    assert repository.search("%' OR 1=1 --") == []
    assert repository.search("%") == []
    assert repository.search("_") == []


@pytest.mark.parametrize("assignment", ["rating = 20", "duration = 0", "mood_id = 999", "genre_id = 999"])
def test_database_constraints_rollback(app, assignment):
    database = app.extensions["database"]
    with pytest.raises(IntegrityError):
        with database.connect() as session:
            session.execute(text(f"UPDATE movies SET {assignment} WHERE id = 1"))
    assert MovieRepository(database).find_by_id(1).rating == 8.3
