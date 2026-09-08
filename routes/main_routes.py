from flask import Blueprint, current_app, render_template, request, redirect, url_for, abort

main = Blueprint("main", __name__)


@main.get("/")
def home():
    engine = current_app.extensions["recommendation_engine"]
    return render_template("index.html", movies=engine.recommend_by_rating()[:5])


@main.route("/recommend", methods=["GET", "POST"])
def recommend():
    name = request.form.get("mood") if request.method == "POST" else request.args.get("mood")
    service = current_app.extensions["movie_service"]
    engine = current_app.extensions["recommendation_engine"]
    try:
        mood = service.resolve_mood(name)
    except ValueError as error:
        return render_template("recommend.html", error=str(error), movies=[], selected_mood=None), 400
    return render_template("recommend.html", selected_mood=mood,
                           movies=engine.recommend_by_mood(mood.name))


@main.get("/random")
def random_movie():
    movie = current_app.extensions["recommendation_engine"].random_movie()
    if movie is None:
        abort(404)
    response = redirect(url_for("movies.detail", movie_id=movie.id))
    response.headers["Cache-Control"] = "no-store"
    return response
