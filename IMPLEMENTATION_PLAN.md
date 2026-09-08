# MoodMovie implementation plan

All five supplied documents were read before source code was created. The overview
is actually named `READEAM.md`; this is the README specification referenced by
`MASTER_PROMPT.md`. Original documents remain untouched.

## Requirements and decisions

- Implement all seven use cases: choose mood, recommendations, catalog, details,
  keyword search, genre filtering, and random discovery. No authentication,
  streaming, payments, or machine learning.
- Follow the explicit black/gold design document and master prompt over the older
  overview's purple/pink visual example.
- Use SQLAlchemy with SQLite, Python/Flask, Jinja, and vanilla CSS/JavaScript.
- Movie belongs to one Mood and one Genre, following the supplied class diagram.
  Seed 24 films, four per mood. Ratings are fixed illustrative demo values.
- User is an actor, not a persisted account. Composition connects services,
  repository, and database; ORM base inheritance supplies persistence behavior.
  Do not invent movie subclasses merely to demonstrate inheritance.
- Movie encapsulates detail/matching behavior. RecommendationEngine sorts matches
  by descending rating with title as a stable tie-breaker and selects random films.
- MovieService validates inputs. MovieRepository owns ORM queries. DatabaseManager
  owns sessions, schema creation, and transactional, idempotent initialization.
- Local vector poster interpretations and local system fonts support offline use.

## Implementation sequence

1. Create models, configuration, database manager, and relational seed data.
2. Build repository, MovieService, RecommendationEngine, and Flask controllers.
3. Build reusable Jinja cards/forms and home, catalog, recommendation, detail,
   search, and error pages. Routes: `/`, `/recommend` (GET/POST), `/movies`,
   `/movie/<id>`, `/search`, `/genre/<genre>`, `/random`.
4. Apply restrained glass navigation/mood panel, gold selection, poster background,
   desktop tilt, scroll reveal, mobile navigation, keyboard focus, reduced motion,
   image fallback, empty results, and input errors. Business logic stays in Python.
5. Test models, repository, initialization, services, all routes, all moods,
   malformed input, no matches, and empty database behavior with pytest.
6. Start actual Flask server; exercise HTTP flows and assets. Use browser automation
   if available to inspect desktop/mobile, focus, motion, links, and image fallback.
7. Fix problems, rerun tests, record final validation, then write and verify RUN.md.

## Planned structure

`app.py`, `config.py`, `requirements.txt`; `models/`, `database/`,
`repositories/`, `services/`, `routes/`, `templates/`, `static/`, `tests/`.
Database tables: `movies`, `moods`, `genres` with foreign keys and value constraints.
