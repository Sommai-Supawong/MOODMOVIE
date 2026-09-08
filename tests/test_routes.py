from pathlib import Path
import pytest


@pytest.mark.parametrize("path,expected", [
    ("/", b"How are you feeling?"), ("/movies", b"24 films"),
    ("/movie/13", b"169 min"), ("/search?q=interstellar", b"1 result"),
    ("/search?q=wormhole", b"Interstellar"), ("/search", b"Enter a title or keyword"),
    ("/search?q=%20%20", b"Enter a title or keyword"),
    ("/search?q=zzzzzzzz", b"No movies found."),
    ("/genre/Sci-Fi", b"3 films"), ("/genre/sci-fi", b"Interstellar"),
])
def test_pages(client, path, expected):
    response = client.get(path)
    assert response.status_code == 200
    assert expected in response.data


@pytest.mark.parametrize("mood", ["Happy", "Sad", "Romantic", "Excited", "Bored", "Relaxed"])
def test_recommendation_routes(client, mood):
    post = client.post("/recommend", data={"mood": mood})
    assert post.status_code == 200
    assert b"4 picks" in post.data
    assert post.data.count(b'class="movie-card"') == 4
    assert client.get(f"/recommend?mood={mood}").status_code == 200


@pytest.mark.parametrize("data", [{}, {"mood": ""}, {"mood": "not-a-mood"}])
def test_invalid_recommendation(client, data):
    response = client.post("/recommend", data=data)
    assert response.status_code == 400
    assert b"Choose one of the six moods" in response.data


@pytest.mark.parametrize("path", ["/movie/0", "/movie/999", "/movie/-1", "/movie/abc", "/movie/999999999999999999999999999", "/missing", "/genre/unknown"])
def test_not_found(client, path):
    response = client.get(path)
    assert response.status_code == 404
    assert b"This scene is missing" in response.data


def test_random_redirect(client):
    response = client.get("/random")
    assert response.status_code == 302
    assert response.headers["Location"].startswith("/movie/")
    assert response.headers["Cache-Control"] == "no-store"
    assert client.get(response.headers["Location"]).status_code == 200


def test_search_input_safety(client):
    response = client.get("/search", query_string={"q": '<script>alert("x")</script>'})
    assert response.status_code == 200
    assert b"<script>alert" not in response.data
    assert b"&lt;script&gt;" in response.data
    assert client.get("/search", query_string={"q": "x" * 101}).status_code == 400
    assert client.post("/recommend", data={"mood": "a" * 17000}).status_code == 413


def test_all_local_assets(client, service):
    for movie in service.get_all_movies():
        response = client.get("/static/" + movie.poster)
        assert response.status_code == 200
        assert "image/svg+xml" in response.content_type
    for path in ["css/style.css", "css/components.css", "css/animations.css", "js/main.js", "images/poster-fallback.svg", "images/favicon.svg"]:
        assert client.get("/static/" + path).status_code == 200


def test_local_asset_references_exist():
    assert len(list(Path("static/images/posters").glob("*.svg"))) == 24
