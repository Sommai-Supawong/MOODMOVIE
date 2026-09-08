"""Small, fixed classroom catalog. Ratings are illustrative, not live scores."""
from sqlalchemy import select
from models import Movie, Mood, Genre

MOODS = [
    ("Happy", "😊", "Keep the good feeling going."),
    ("Sad", "😢", "A little room to feel it all."),
    ("Romantic", "❤️", "For the hopeful at heart."),
    ("Excited", "🔥", "Make tonight an adventure."),
    ("Bored", "😴", "Something out of the ordinary."),
    ("Relaxed", "😌", "Slow down. Settle into a story."),
]

# title, year, demo rating, minutes, primary mood, primary genre, synopsis
MOVIES = [
    ("Toy Story", 1995, 8.3, 81, "Happy", "Animation", "A beloved cowboy toy and a new space ranger must put their rivalry aside to find their way home."),
    ("Paddington 2", 2017, 7.8, 103, "Happy", "Comedy", "A kindhearted bear takes on odd jobs to buy a special gift, only to become tangled in a wonderfully peculiar theft."),
    ("The Grand Budapest Hotel", 2014, 8.1, 99, "Happy", "Comedy", "A meticulous concierge and his young lobby boy are swept into a caper involving a missing painting and a changing Europe."),
    ("Singin' in the Rain", 1952, 8.3, 103, "Happy", "Comedy", "As silent movies give way to sound, three performers turn a troubled production into a joyful musical reinvention."),
    ("The Pursuit of Happyness", 2006, 8.0, 117, "Sad", "Drama", "A father facing homelessness holds onto his bond with his son while pursuing a chance at a more stable life."),
    ("The Notebook", 2004, 7.8, 123, "Sad", "Romance", "An old notebook brings a summer romance back to life, tracing a love tested by distance, class, and time."),
    ("Inside Out", 2015, 8.1, 95, "Sad", "Animation", "Inside a young girl's mind, Joy and Sadness discover why growing up needs more than one emotion."),
    ("Good Will Hunting", 1997, 8.3, 126, "Sad", "Drama", "A gifted young janitor begins to confront the wounds holding him back with help from an unconventional therapist."),
    ("La La Land", 2016, 8.0, 128, "Romantic", "Romance", "An aspiring actress and a jazz pianist fall in love in Los Angeles while trying to make room for their dreams."),
    ("About Time", 2013, 7.8, 123, "Romantic", "Romance", "A young man who can revisit moments in his life learns that love lies in the ordinary days as much as the perfect ones."),
    ("Before Sunrise", 1995, 8.1, 101, "Romantic", "Romance", "Two strangers leave a train in Vienna and spend one night walking, talking, and imagining a life beyond the morning."),
    ("Pride & Prejudice", 2005, 7.8, 129, "Romantic", "Drama", "A spirited young woman and a reserved gentleman must look beyond first impressions in the English countryside."),
    ("Interstellar", 2014, 8.7, 169, "Excited", "Sci-Fi", "With Earth's future in doubt, a former pilot joins a mission through a wormhole, leaving his family behind to search for a new home."),
    ("Inception", 2010, 8.8, 148, "Excited", "Sci-Fi", "A specialist in stealing secrets from dreams takes on the reverse challenge: planting an idea deep inside a sleeping mind."),
    ("Mad Max: Fury Road", 2015, 8.1, 120, "Excited", "Action", "Two reluctant allies lead a desperate escape across a desert wasteland in a convoy pursued by a ruthless ruler."),
    ("Spider-Man: Into the Spider-Verse", 2018, 8.4, 117, "Excited", "Animation", "Brooklyn teenager Miles Morales meets heroes from other dimensions and discovers what it means to become his own Spider-Man."),
    ("Knives Out", 2019, 7.9, 130, "Bored", "Mystery", "A detective investigates a novelist's death, finding that every member of a wealthy family has a different story to tell."),
    ("The Prestige", 2006, 8.5, 130, "Bored", "Mystery", "Two stage magicians turn professional rivalry into an all-consuming contest of secrets, sacrifice, and illusion."),
    ("The Martian", 2015, 8.0, 144, "Bored", "Sci-Fi", "Stranded on Mars, an astronaut uses science, resourcefulness, and humor to survive while Earth plans a rescue."),
    ("The Truman Show", 1998, 8.2, 103, "Bored", "Drama", "An ordinary man's picture-perfect town begins to reveal unsettling cracks, leading him to question the world around him."),
    ("Spirited Away", 2001, 8.6, 125, "Relaxed", "Animation", "A girl enters a bathhouse for spirits and finds courage, friendship, and a way to save her transformed parents."),
    ("My Neighbor Totoro", 1988, 8.1, 86, "Relaxed", "Animation", "Two sisters move to the countryside and discover gentle woodland spirits as they adjust to a new home."),
    ("The Secret Life of Walter Mitty", 2013, 7.3, 114, "Relaxed", "Adventure", "A quiet photo archivist steps beyond his daydreams on a journey through remarkable landscapes to find a missing negative."),
    ("Chef", 2014, 7.3, 114, "Relaxed", "Comedy", "A chef starts again with a food truck, rediscovering the pleasure of cooking and reconnecting with his son on the road."),
]


def seed_database(session):
    moods = {m.name: m for m in session.scalars(select(Mood))}
    genres = {g.name: g for g in session.scalars(select(Genre))}
    for name, emoji, description in MOODS:
        if name not in moods:
            moods[name] = Mood(name=name, emoji=emoji, description=description)
            session.add(moods[name])
    for name in sorted({row[5] for row in MOVIES}):
        if name not in genres:
            genres[name] = Genre(name=name)
            session.add(genres[name])
    for index, (title, year, rating, duration, mood, genre, description) in enumerate(MOVIES, 1):
        session.add(Movie(
            title=title, release_year=year, rating=rating, duration=duration,
            mood=moods[mood], genre=genres[genre], description=description,
            poster=f"images/posters/{index:02d}.svg",
        ))
