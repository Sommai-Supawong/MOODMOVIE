"""Deployment contracts: factory startup, fresh state, and Linux path spelling."""
import ast
import importlib
from html.parser import HTMLParser
from pathlib import Path

from flask import Flask
from jinja2 import meta
from sqlalchemy import delete

from app import create_app
from models import Movie

ROOT = Path(__file__).resolve().parents[1]


def test_factory_entry_point_and_debug(app):
    module = importlib.import_module("app")
    assert Path(module.__file__).resolve() == ROOT / "app.py"
    assert callable(module.create_app)
    assert isinstance(app, Flask)
    assert callable(app.wsgi_app)
    assert not app.debug


def test_fresh_start_and_repeat_start_preserve_catalog(tmp_path):
    path = tmp_path / "new" / "nested" / "catalog.db"
    assert not path.parent.exists()
    settings = {"TESTING": True, "DATABASE_PATH": str(path)}
    first = create_app(settings)
    try:
        assert path.is_file()
        service = first.extensions["movie_service"]
        assert (len(service.get_all_movies()), len(service.get_moods()), len(service.get_genres())) == (24, 6, 8)
        assert first.test_client().get("/").status_code == 200
        assert first.test_client().post("/recommend", data={"mood": "Happy"}).status_code == 200
        # Existing data must survive later initialization without being overwritten.
        with first.extensions["database"].connect() as session:
            session.get(Movie, 1).description = "Preserved across restart"
    finally:
        first.extensions["database"].close()
    second = create_app(settings)
    try:
        service = second.extensions["movie_service"]
        assert (len(service.get_all_movies()), len(service.get_moods()), len(service.get_genres())) == (24, 6, 8)
        assert service.get_movie_by_id(1).description == "Preserved across restart"
    finally:
        second.extensions["database"].close()


def test_empty_movies_reseed_without_duplicate_classifications(app):
    database = app.extensions["database"]
    with database.connect() as session:
        session.execute(delete(Movie))
    database.initialize()
    database.initialize()
    service = app.extensions["movie_service"]
    assert (len(service.get_all_movies()), len(service.get_moods()), len(service.get_genres())) == (24, 6, 8)


def assert_exact_case(path):
    """Windows exists() alone cannot detect a path that will fail on Linux."""
    relative = path.relative_to(ROOT)
    directory = ROOT
    for part in relative.parts:
        assert part in {item.name for item in directory.iterdir()}, str(relative)
        directory /= part
    assert directory.is_file(), str(relative)


def test_python_imports_and_template_case(app):
    local_modules = {"app", "config", "models", "routes", "services", "repositories", "database"}
    sources = [ROOT / "app.py", ROOT / "config.py"]
    for folder in local_modules - {"app", "config"}:
        sources.extend((ROOT / folder).glob("*.py"))
    for source in sources:
        tree = ast.parse(source.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            names = [node.module] if isinstance(node, ast.ImportFrom) and node.module else []
            if isinstance(node, ast.Import):
                names = [alias.name for alias in node.names]
            for name in names:
                if name.split('.')[0].casefold() in local_modules:
                    path = ROOT.joinpath(*name.split('.'))
                    assert_exact_case(path / "__init__.py" if path.is_dir() else path.with_suffix('.py'))
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "render_template":
                assert_exact_case(ROOT / "templates" / ast.literal_eval(node.args[0]))
    for name in app.jinja_env.list_templates():
        assert_exact_case(ROOT / "templates" / name)
        source, _, _ = app.jinja_env.loader.get_source(app.jinja_env, name)
        for reference in meta.find_referenced_templates(app.jinja_env.parse(source)):
            assert reference is not None, "Audit dynamic template references explicitly"
            assert_exact_case(ROOT / "templates" / reference)
        app.jinja_env.get_template(name)


class StaticReferences(HTMLParser):
    def __init__(self):
        super().__init__()
        self.paths = set()

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name in {"src", "href", "data-fallback"} and value and value.startswith("/static/"):
                self.paths.add(value)


def test_rendered_static_paths_use_exact_case(client, service):
    paths = ["/", "/movies", "/search", "/missing"]
    paths += [f"/movie/{movie.id}" for movie in service.get_all_movies()]
    paths += [f"/recommend?mood={mood.name}" for mood in service.get_moods()]
    paths += [f"/genre/{genre.name}" for genre in service.get_genres()]
    references = StaticReferences()
    for path in paths:
        references.feed(client.get(path).get_data(as_text=True))
    assert len(references.paths) == 30  # 24 posters, fallback, icon, 3 CSS, JS.
    for reference in references.paths:
        assert_exact_case(ROOT / reference.lstrip('/'))
        assert client.get(reference).status_code == 200


def test_portable_default_database_path_from_other_directory(tmp_path, monkeypatch):
    from config import Config
    monkeypatch.chdir(tmp_path)
    # The override, if supplied by the caller, is intentionally not constrained.
    import os
    if "MOODMOVIE_DATABASE" not in os.environ:
        assert Path(Config.DATABASE_PATH).is_absolute()
        assert Path(Config.DATABASE_PATH) == ROOT / "database" / "moodmovie.db"
