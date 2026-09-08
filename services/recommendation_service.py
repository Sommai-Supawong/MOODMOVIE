import random


class RecommendationEngine:
    """Explainable rules: match the assigned mood, then rank by demo rating."""

    def __init__(self, movie_service):
        self._movie_service = movie_service

    @staticmethod
    def _rank(movies):
        return sorted(movies, key=lambda movie: (-movie.get_rating(), movie.title.casefold()))

    def recommend_by_mood(self, mood):
        return self._rank(self._movie_service.get_movies_by_mood(mood))

    def recommend_by_rating(self):
        return self._rank(self._movie_service.get_all_movies())

    def random_movie(self):
        movies = self._movie_service.get_all_movies()
        return random.choice(movies) if movies else None
