import pytest
from app import create_app


@pytest.mark.parametrize("mood", ["Happy", "Sad", "Romantic", "Excited", "Bored", "Relaxed"])
def test_recommendations_match_and_rank(engine, mood):
    movies = engine.recommend_by_mood(mood.lower())
    assert len(movies) == 4
    assert all(movie.match_mood(mood) for movie in movies)
    assert [movie.rating for movie in movies] == sorted([movie.rating for movie in movies], reverse=True)


@pytest.mark.parametrize("mood", [None, "", "unknown", "%' OR 1=1 --"])
def test_invalid_mood(engine, mood):
    with pytest.raises(ValueError):
        engine.recommend_by_mood(mood)


def test_rank_tie_and_random(engine, service):
    happy = engine.recommend_by_mood("Happy")
    assert [m.title for m in happy[:2]] == ["Singin' in the Rain", "Toy Story"]
    assert engine.recommend_by_rating()[0].title == "Inception"
    valid = {m.id for m in service.get_all_movies()}
    for _ in range(20):
        assert engine.random_movie().id in valid


def test_empty_catalog(tmp_path):
    app = create_app({"TESTING": True, "DATABASE_PATH": str(tmp_path / "empty.db"), "SEED_DATABASE": False})
    try:
        engine = app.extensions["recommendation_engine"]
        assert engine.random_movie() is None
        assert engine.recommend_by_rating() == []
        client = app.test_client()
        assert client.get("/").status_code == 200
        assert b"No movies are available" in client.get("/movies").data
        assert client.get("/random").status_code == 404
    finally:
        app.extensions["database"].close()
