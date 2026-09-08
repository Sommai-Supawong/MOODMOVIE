from flask import Blueprint, current_app, render_template, request, abort

movies = Blueprint("movies", __name__)


def service():
    return current_app.extensions["movie_service"]


@movies.get("/movies")
def catalog():
    return render_template("movies.html", movies=service().get_all_movies(), selected_genre=None)


@movies.get("/movie/<int:movie_id>")
def detail(movie_id):
    movie = service().get_movie_by_id(movie_id)
    if movie is None:
        abort(404)
    engine = current_app.extensions["recommendation_engine"]
    similar = [m for m in engine.recommend_by_mood(movie.mood.name) if m.id != movie.id][:4]
    return render_template("movie_detail.html", movie=movie, similar=similar)


@movies.get("/search")
def search():
    query = request.args.get("q", "").strip()
    try:
        results = service().search_movie(query)
    except ValueError as error:
        return render_template("search_results.html", movies=[], query=query[:100], error=str(error)), 400
    return render_template("search_results.html", movies=results, query=query)


@movies.get("/genre/<genre>")
def genre(genre):
    selected = service().resolve_genre(genre)
    if selected is None:
        abort(404)
    return render_template("movies.html", movies=service().filter_by_genre(selected.name), selected_genre=selected)
