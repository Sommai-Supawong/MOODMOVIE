"""Portable defaults; tests can supply a separate database."""
import os
from pathlib import Path


class Config:
    DATABASE_PATH = os.environ.get(
        "MOODMOVIE_DATABASE", str(Path(__file__).parent / "database" / "moodmovie.db")
    )
    SEED_DATABASE = True
    MAX_CONTENT_LENGTH = 16 * 1024
