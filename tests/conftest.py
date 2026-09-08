import pytest
from app import create_app


@pytest.fixture
def app(tmp_path):
    app = create_app({"TESTING": True, "DATABASE_PATH": str(tmp_path / "test.db")})
    yield app
    app.extensions["database"].close()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def service(app):
    return app.extensions["movie_service"]


@pytest.fixture
def engine(app):
    return app.extensions["recommendation_engine"]
