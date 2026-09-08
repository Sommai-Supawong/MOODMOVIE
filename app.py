"""Application composition root. Run with python app.py."""
import os
from flask import Flask, render_template
from config import Config
from database.database import DatabaseManager
from repositories.movie_repository import MovieRepository
from services.movie_service import MovieService
from services.recommendation_service import RecommendationEngine


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)
    if test_config:
        app.config.update(test_config)

    database = DatabaseManager(app.config["DATABASE_PATH"])
    database.initialize(seed=app.config["SEED_DATABASE"])
    service = MovieService(MovieRepository(database))
    app.extensions.update(database=database, movie_service=service,
                          recommendation_engine=RecommendationEngine(service))

    from routes.main_routes import main
    from routes.movie_routes import movies
    app.register_blueprint(main)
    app.register_blueprint(movies)

    @app.context_processor
    def catalog_navigation():
        return dict(moods=service.get_moods(), genres=service.get_genres())

    @app.errorhandler(404)
    def not_found(_error):
        return render_template("error.html", code=404, title="This scene is missing.",
                               message="We couldn't find that page or movie. A different story is waiting."), 404

    @app.errorhandler(413)
    def too_large(_error):
        return render_template("error.html", code=413, title="A little too much detail.",
                               message="Please try a shorter request."), 413

    return app


if __name__ == "__main__":
    create_app().run(host="127.0.0.1", port=int(os.environ.get("PORT", "5000")))
