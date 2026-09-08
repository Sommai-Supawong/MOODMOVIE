import pytest


def test_movie_service(service):
    assert len(service.get_all_movies()) == 24
    assert service.get_movie_by_id(1).title == "Toy Story"
    assert service.search_movie("  INTERSTELLAR ")[0].id == 13
    assert service.search_movie("  ") == []
    assert service.search_movie("no such film") == []
    assert service.resolve_genre(" sci-fi ").name == "Sci-Fi"
    assert len(service.filter_by_genre("Sci-Fi")) == 3
    assert service.filter_by_genre("Unknown") == []
    with pytest.raises(ValueError):
        service.search_movie("a" * 101)


@pytest.mark.parametrize("movie_id", [0, -1, 999, 2**100, None, "one"])
def test_invalid_movie_ids(service, movie_id):
    assert service.get_movie_by_id(movie_id) is None
