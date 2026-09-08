class MovieService:
    """Validate catalog input and coordinate repository access."""

    def __init__(self, repository):
        self._repository = repository

    def get_all_movies(self):
        return self._repository.find_all()

    def get_movie_by_id(self, movie_id):
        if not isinstance(movie_id, int) or not 0 < movie_id <= 2**63 - 1:
            return None
        return self._repository.find_by_id(movie_id)

    def search_movie(self, keyword):
        keyword = (keyword or "").strip()
        if len(keyword) > 100:
            raise ValueError("Please keep your search to 100 characters or fewer.")
        return self._repository.search(keyword) if keyword else []

    def get_moods(self):
        return self._repository.get_moods()

    def get_genres(self):
        return self._repository.get_genres()

    def resolve_mood(self, name):
        normalized = (name or "").strip().casefold()
        mood = next((m for m in self.get_moods() if m.name.casefold() == normalized), None)
        if mood is None:
            raise ValueError("Choose one of the six moods below to find your next movie.")
        return mood

    def get_movies_by_mood(self, mood):
        return self._repository.find_by_mood(self.resolve_mood(mood).name)

    def resolve_genre(self, name):
        normalized = (name or "").strip().casefold()
        return next((g for g in self.get_genres() if g.name.casefold() == normalized), None)

    def filter_by_genre(self, genre):
        resolved = self.resolve_genre(genre)
        return self._repository.find_by_genre(resolved.name) if resolved else []
