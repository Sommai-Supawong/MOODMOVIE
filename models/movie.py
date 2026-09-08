from sqlalchemy import CheckConstraint, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models import Base
from models.mood import Mood
from models.genre import Genre


class Movie(Base):
    """A film and its primary mood/genre classification."""

    __tablename__ = "movies"
    __table_args__ = (
        CheckConstraint("rating >= 0 AND rating <= 10"),
        CheckConstraint("duration > 0"),
        CheckConstraint("release_year >= 1888"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), unique=True)
    description: Mapped[str] = mapped_column(Text)
    release_year: Mapped[int]
    rating: Mapped[float]
    duration: Mapped[int]
    poster: Mapped[str] = mapped_column(String(300))
    mood_id: Mapped[int] = mapped_column(ForeignKey("moods.id"), index=True)
    genre_id: Mapped[int] = mapped_column(ForeignKey("genres.id"), index=True)
    mood: Mapped[Mood] = relationship(lazy="joined")
    genre: Mapped[Genre] = relationship(lazy="joined")

    def match_mood(self, mood):
        name = mood.name if isinstance(mood, Mood) else mood
        return isinstance(name, str) and self.mood.name.casefold() == name.strip().casefold()

    def get_rating(self):
        return self.rating

    def get_detail(self):
        return {
            "id": self.id, "title": self.title, "description": self.description,
            "release_year": self.release_year, "rating": self.rating,
            "duration": self.duration, "poster": self.poster,
            "mood": self.mood.name, "genre": self.genre.name,
        }
