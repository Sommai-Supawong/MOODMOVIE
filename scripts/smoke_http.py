"""Exercise the running server with the standard library, not Flask's test client."""
import sys
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import urlopen


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:5000"
    checks = 0
    cases = [
        ("/", 200, "How are you feeling?"),
        ("/movies", 200, "24 films"),
        ("/movie/13", 200, "169 min"),
        ("/movie/999", 404, "This scene is missing"),
        ("/search?q=interstellar", 200, "1 result"),
        ("/search", 200, "Enter a title or keyword"),
        ("/search?q=zzzzzzz", 200, "No movies found"),
        ("/genre/Sci-Fi", 200, "3 films"),
        ("/random", 200, "TONIGHT’S FEATURE"),
        ("/static/css/style.css", 200, "--gold"),
        ("/static/css/components.css", 200, ".mood-grid"),
        ("/static/css/animations.css", 200, "prefers-reduced-motion"),
        ("/static/js/main.js", 200, "IntersectionObserver"),
    ]
    for path, status, expected in cases:
        try:
            response = urlopen(base + path, timeout=10)
        except HTTPError as error:
            response = error
        with response:
            assert response.status == status, path
            assert expected in response.read().decode("utf-8"), path
        checks += 1
    for mood in ["Happy", "Sad", "Romantic", "Excited", "Bored", "Relaxed"]:
        with urlopen(base + "/recommend", data=urlencode({"mood": mood}).encode(), timeout=10) as response:
            assert response.status == 200
            assert "4 picks" in response.read().decode("utf-8")
        checks += 1
    print(f"PASS: {checks} real-server HTTP checks at {base}")


if __name__ == "__main__":
    main()
