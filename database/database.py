"""Connection lifecycle and first-run initialization."""
from contextlib import contextmanager
from pathlib import Path
from sqlalchemy import URL, create_engine, event, select, func
from sqlalchemy.orm import Session
from models import Base, Movie


class DatabaseManager:
    def __init__(self, database_path):
        path = Path(database_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        self.engine = create_engine(URL.create("sqlite", database=str(path)))
        event.listen(self.engine, "connect", self._enable_foreign_keys)

    @staticmethod
    def _enable_foreign_keys(connection, _record):
        cursor = connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

    @contextmanager
    def connect(self):
        """Each operation owns a session; exceptions roll back and always close."""
        with Session(self.engine, expire_on_commit=False) as session:
            with session.begin():
                yield session

    def initialize(self, seed=True):
        Base.metadata.create_all(self.engine)
        if seed:
            from database.seed import seed_database
            with self.connect() as session:
                if session.scalar(select(func.count()).select_from(Movie)) == 0:
                    seed_database(session)

    def close(self):
        self.engine.dispose()
