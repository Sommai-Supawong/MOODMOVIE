def test_movie_detail_and_rating(service):
    movie = service.get_movie_by_id(13)
    assert movie.title == "Interstellar"
    assert movie.get_rating() == 8.7
    assert movie.get_detail() == {
        "id": 13, "title": "Interstellar", "description": movie.description,
        "release_year": 2014, "rating": 8.7, "duration": 169,
        "poster": "images/posters/13.svg", "mood": "Excited", "genre": "Sci-Fi",
    }


def test_mood_matching(service):
    movie = service.get_movie_by_id(1)
    assert movie.match_mood("  HAPPY  ")
    assert movie.match_mood(movie.mood)
    assert not movie.match_mood("Sad")
    assert not movie.match_mood(None)
    assert movie.mood.get_name() == "Happy"
    assert movie.mood.get_emoji() == "😊"
    assert movie.genre.get_name() == "Animation"
