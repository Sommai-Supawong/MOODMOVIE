from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from models import Base


class Mood(Base):
    __tablename__ = "moods"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True)
    emoji: Mapped[str] = mapped_column(String(10))
    description: Mapped[str] = mapped_column(String(150))

    def get_name(self):
        return self.name

    def get_emoji(self):
        return self.emoji
