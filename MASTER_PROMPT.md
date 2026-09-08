You are the lead software engineer responsible for building the complete
"MoodMovie — Movie Recommendation by Mood" mini project.

Your goal is to read and analyze all project specification files in the current
workspace, design the application according to OOAD and OOP principles, implement
the full working web application, test it, fix discovered issues, and finally
create RUN.md containing complete instructions for running the project.

IMPORTANT:
Do not immediately start coding.

First inspect and understand the entire project specification.

==================================================
PROJECT DOCUMENTS
==================================================

The current project root contains these specification files:

- README.md
- MoodMovie_Class_Diagram.md
- MoodMovie_Use_Case.md
- MoodMovie_design.md

You MUST read all four files completely before modifying or creating source code.

Use them as the primary source of truth.

Interpret them as follows:

README.md
→ Overall project requirements, features, architecture, technology stack,
  project scope, database concepts, Flask flow, and expected functionality.

MoodMovie_Class_Diagram.md
→ OOAD class responsibilities, relationships, service layer,
  repository/data access concepts, and OOP structure.

MoodMovie_Use_Case.md
→ Actor, use cases, user flows, preconditions, postconditions,
  expected behavior, and functional requirements.

MoodMovie_design.md
→ UI/UX design system, color palette, dark cinematic visual direction,
  glass UI, liquid glass, animation, responsive behavior,
  3D hover interactions, and visual constraints.

If documents contain small inconsistencies, resolve them using this priority:

1. Functional correctness and project scope from README.md
2. Use cases from MoodMovie_Use_Case.md
3. OOAD architecture from MoodMovie_Class_Diagram.md
4. Visual implementation from MoodMovie_design.md

Do not implement unnecessary functionality outside the Mini Project scope.

==================================================
PRIMARY OBJECTIVE
==================================================

Build a complete working web application:

MoodMovie
"Find a movie that matches your mood."

The user should be able to:

1. Open the website
2. Select a mood
3. Receive movie recommendations based on that mood
4. Browse all movies
5. View movie details
6. Search for movies
7. Filter movies by genre
8. Use "Surprise Me" to receive a random movie

The application must demonstrate:

- OOAD
- OOP
- Python
- Flask
- HTML
- CSS
- JavaScript
- Jinja2
- SQLite
- clean software architecture

==================================================
TECH STACK
==================================================

Use:

Backend:
- Python
- Flask

Frontend:
- HTML5
- CSS3
- Vanilla JavaScript
- Jinja2

Database:
- SQLite

Testing:
- pytest
- Flask test client where appropriate

Do NOT introduce React, Vue, Angular, Node frontend tooling,
or another major framework unless absolutely required.

Keep the project appropriate for a university-level Mini Project.

==================================================
DEVELOPMENT PHILOSOPHY
==================================================

This project must clearly demonstrate OOAD and OOP.

Do not place all logic inside app.py.

Avoid procedural spaghetti code.

Use separation of concerns.

Recommended architecture:

Presentation Layer
    ↓
Flask Routes / Controllers
    ↓
Service Layer
    ↓
Domain Models
    ↓
Repository / Data Access
    ↓
SQLite Database

The final code should be understandable enough to explain during a presentation.

Avoid unnecessary enterprise-level abstractions.

The architecture should be clean but not overengineered.

==================================================
PHASE 1 — PROJECT ANALYSIS
==================================================

Before coding:

1. Read all specification Markdown files.
2. Inspect the current directory and existing files.
3. Determine the complete functional requirements.
4. Determine the required entities/classes.
5. Determine relationships between classes.
6. Determine required Flask routes.
7. Determine the required database schema.
8. Determine the required HTML pages.
9. Determine service responsibilities.
10. Determine repository/data-access responsibilities.
11. Determine the testing strategy.
12. Determine which UI interactions require JavaScript.

Create an internal implementation plan.

Before implementation, output a concise summary in the terminal containing:

- Main requirements
- Main classes
- Main routes
- Database tables
- Pages
- Planned project structure

Then continue automatically.

Do not stop to ask for confirmation unless there is a genuine blocking issue.

==================================================
PHASE 2 — OOAD AND OOP DESIGN
==================================================

Design the implementation based on the supplied class diagram.

The core concepts should include, when appropriate:

Movie
Mood
Genre
RecommendationEngine
MovieService
MovieRepository
DatabaseManager

User may exist as a domain concept if useful, but a real login/account system
is NOT required for this Mini Project.

Each class must have a clear responsibility.

Examples:

Movie
→ Movie domain entity.

Mood
→ Represents supported moods.

Genre
→ Represents movie genres.

RecommendationEngine
→ Responsible for recommendation logic.

MovieService
→ Coordinates movie-related business logic.

MovieRepository
→ Handles movie persistence and database queries.

DatabaseManager
→ Handles SQLite connection/database initialization if needed.

Apply OOP concepts naturally:

- Class
- Object
- Attributes
- Methods
- Encapsulation
- Abstraction
- Composition
- Appropriate inheritance/polymorphism only when it genuinely improves design

IMPORTANT:

Do NOT force inheritance or polymorphism into areas where it makes the code worse.

The project should demonstrate good OOP, not artificial OOP.

==================================================
PHASE 3 — PROJECT STRUCTURE
==================================================

Create a clean project structure.

A suitable starting structure could be:

MOODMOVIE/
│
├── app.py
├── config.py
├── requirements.txt
│
├── models/
│   ├── __init__.py
│   ├── movie.py
│   ├── mood.py
│   └── genre.py
│
├── services/
│   ├── __init__.py
│   ├── movie_service.py
│   └── recommendation_service.py
│
├── repositories/
│   ├── __init__.py
│   └── movie_repository.py
│
├── database/
│   ├── __init__.py
│   ├── database.py
│   └── moodmovie.db
│
├── routes/
│   ├── __init__.py
│   ├── main_routes.py
│   └── movie_routes.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── movies.html
│   ├── recommend.html
│   ├── movie_detail.html
│   ├── search_results.html
│   └── 404.html
│
├── static/
│   ├── css/
│   │   ├── style.css
│   │   ├── components.css
│   │   └── animations.css
│   │
│   ├── js/
│   │   └── main.js
│   │
│   └── images/
│
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_services.py
│   ├── test_recommendation.py
│   └── test_routes.py
│
├── README.md
├── MoodMovie_Class_Diagram.md
├── MoodMovie_Use_Case.md
├── MoodMovie_design.md
└── RUN.md

You may adjust this structure if there is a strong architectural reason.

Do not delete the original specification Markdown files.

==================================================
PHASE 4 — DATABASE
==================================================

Use SQLite.

Create a database initialization mechanism so a new user can run the project
without manually creating database tables.

At minimum represent:

movies
moods
genres

Choose a relational structure that is appropriate for the project.

Seed the database with enough demo data to make the interface meaningful.

Recommended minimum:

- at least 18–24 movies
- multiple movies for each supported mood
- several genres

Supported moods should include:

Happy
Sad
Romantic
Excited
Bored
Relaxed

Use appropriate emojis only where they fit the UI.

Movie data should include fields similar to:

id
title
description
release_year
rating
duration
poster
mood
genre

If using remote poster URLs, the UI must handle missing or failed images gracefully.

Prefer a reliable placeholder/fallback rather than breaking the layout.

Do not require external API keys.

The core application must work offline except for remote assets if any.

==================================================
PHASE 5 — RECOMMENDATION ENGINE
==================================================

The initial MoodMovie recommendation system should be rule-based.

Machine Learning is NOT required.

Example:

User chooses:

Happy

RecommendationEngine
→ receives mood
→ asks MovieService for matching movies
→ obtains Movie objects
→ optionally sorts them by rating
→ returns recommendations

Keep the algorithm simple enough to explain in a classroom presentation.

Recommendation logic must not be implemented directly inside HTML templates.

Recommendation logic belongs in Python domain/service classes.

"Surprise Me" should return a valid random movie.

==================================================
PHASE 6 — FLASK ROUTES
==================================================

Implement clear routes.

Expected route concepts include:

GET /
→ Homepage

POST /recommend
→ Mood recommendation

GET /movies
→ All movies

GET /movie/<id>
→ Movie details

GET /search
→ Movie search

GET /genre/<genre>
→ Genre filtering

GET /random
→ Surprise Me

Exact route naming may be improved if necessary,
but the use cases must remain supported.

Validate request values.

Handle invalid movie IDs gracefully.

Implement an appropriate 404 page.

==================================================
PHASE 7 — UI / UX IMPLEMENTATION
==================================================

Read MoodMovie_design.md carefully before implementing the interface.

The primary style is:

Dark Cinematic
+
Premium Gold
+
Glass UI
+
Liquid Glass
+
Subtle 3D Interaction
+
Smooth Animation

Primary background:
almost black / graphite.

Primary accent:
yellow gold / premium gold.

Use the design tokens from MoodMovie_design.md where practical.

==================================================
IMPORTANT UI CONSTRAINT
==================================================

The website must NOT look excessively AI-generated.

Avoid the common "AI-generated landing page" appearance.

Specifically avoid:

- excessive gradients everywhere
- too many glowing objects
- giant unnecessary text
- excessive floating decorative blobs
- random abstract spheres
- excessive emoji decoration
- excessive glass on every element
- neon cyberpunk appearance
- unnecessary complex animations
- enormous rounded cards everywhere
- identical generic SaaS sections
- overcrowded effects

Instead aim for:

- cinematic
- restrained
- editorial
- premium
- intentional
- visually balanced
- human-designed
- clean spacing
- clear hierarchy

Reference feeling:

premium movie discovery interface,
not an AI startup landing page.

==================================================
VISUAL STYLE
==================================================

Main colors:

Background:
#070707

Secondary:
#111111

Primary Gold:
#F5C451

Gold Highlight:
#FFD76A

Dark Gold:
#C99A2E

Primary Text:
#F5F5F5

Secondary Text:
#B5B5B5

Glass:
rgba(255,255,255,0.06)

Use gold selectively.

Gold should emphasize:

- CTA buttons
- selected mood
- selected filter
- rating
- active navigation
- subtle highlights

Do not make every text element gold.

==================================================
GLASS UI
==================================================

Use glass effects mainly for:

- Navbar
- Mood selector
- Search interface
- Movie detail information panel
- Modal/floating control when needed

Do not apply heavy backdrop blur to every movie card.

Movie posters should remain visually dominant.

==================================================
MOVIE BACKGROUND
==================================================

The homepage should have a cinematic moving movie-poster background.

Requirements:

- blurred or darkened
- low opacity
- slow motion
- should not reduce text readability
- should not cause distracting visual noise

A horizontal moving poster strip or layered poster wall is acceptable.

Use CSS animation where possible.

Make it seamless if practical.

The animation should feel slow and cinematic.

==================================================
3D INTERACTION
==================================================

Use subtle 3D movement for:

Mood Cards
Movie Cards
Movie Detail Poster

Mouse movement may create:

rotateX
rotateY
translateY
scale

Keep rotation small.

Recommended maximum:
approximately 3–8 degrees.

The effect should enhance depth, not become a gimmick.

==================================================
HOVER BEHAVIOR
==================================================

Mood Card hover:

- slight lift
- subtle 3D tilt
- gold border
- small glow
- emoji/icon movement

Movie Card hover:

- slight poster zoom
- slight elevation
- information overlay
- subtle tilt
- View Details action reveal

Buttons:

- small translateY
- slight scale
- controlled gold shadow

Everything should use smooth transitions.

==================================================
ANIMATION
==================================================

Motion should follow this philosophy:

Smooth
Subtle
Purposeful
Premium

Suggested timing:

Micro interaction:
150–250ms

Hover:
250–400ms

Card transition:
350–500ms

Section reveal:
500–800ms

Background movement:
20–60 seconds

Prefer CSS transforms and opacity.

Avoid animations that trigger excessive layout recalculation.

==================================================
PAGE INTRO
==================================================

Suggested initial sequence:

Background fade
→ Logo/navigation appears
→ Hero title moves upward slightly
→ Subtitle fades in
→ CTA appears
→ Mood cards reveal

Use subtle staggered timing.

Do not create a long intro that delays interaction.

==================================================
SCROLL EFFECT
==================================================

Implement simple scroll reveal for important sections.

Use IntersectionObserver instead of heavy libraries.

Example behavior:

opacity 0
translateY(24px)

→ enters viewport →

opacity 1
translateY(0)

==================================================
MOUSE SPOTLIGHT
==================================================

A very subtle mouse-following gold spotlight may be added to desktop.

Keep opacity extremely low.

It should disappear or be disabled on touch/mobile devices.

==================================================
RESPONSIVE DESIGN
==================================================

The application must work on:

Desktop
Laptop
Tablet
Mobile

Recommended movie grid behavior:

Desktop:
4–5 columns

Laptop:
3–4 columns

Tablet:
2–3 columns

Mobile:
2 columns where practical
or 1 column for detail-heavy cards.

Navigation should become mobile-friendly.

Do not rely on hover for essential functionality.

==================================================
ACCESSIBILITY
==================================================

Ensure:

- adequate color contrast
- visible keyboard focus
- semantic HTML
- proper button elements
- meaningful alt attributes
- forms have labels
- reduced-motion support

Implement:

@media (prefers-reduced-motion: reduce)

Reduce or disable nonessential animation.

==================================================
PHASE 8 — FRONTEND JAVASCRIPT
==================================================

Use Vanilla JavaScript.

JavaScript should handle only interactive behavior such as:

- 3D card tilt
- cursor spotlight
- navigation menu
- scroll reveal
- optional carousel controls
- UI transition helpers

Business logic must remain on the Python side.

Do not duplicate recommendation logic in JavaScript.

Avoid large external JS libraries unless required.

==================================================
PHASE 9 — CODE QUALITY
==================================================

Write clean and understandable Python.

Requirements:

- meaningful names
- small focused methods
- docstrings where useful
- no giant functions
- no duplicated business logic
- clear imports
- sensible module organization
- no hardcoded absolute local paths
- use configuration where appropriate

Keep code understandable to a student studying OOAD/OOP.

Do not overuse design patterns.

==================================================
PHASE 10 — TESTING
==================================================

After implementation, do NOT assume the project works.

Run tests.

Create automated tests covering at minimum:

1. Movie model behavior
2. Mood matching
3. Recommendation logic
4. MovieService
5. MovieRepository where practical
6. Homepage route
7. Recommendation POST route
8. Movies route
9. Movie detail route
10. Search route
11. Genre filter
12. Random movie route
13. Invalid movie / 404 behavior

Use pytest.

Run:

pytest

Fix failing tests.

Repeat until the test suite passes.

Do not leave knowingly failing tests.

==================================================
PHASE 11 — APPLICATION RUN TEST
==================================================

After automated tests pass:

Start the real Flask application.

Verify that it starts without exceptions.

Test the website as a user.

At minimum validate:

Homepage:
- loads successfully
- styles load
- JavaScript loads
- mood cards render

Mood recommendation:
- selecting each mood works
- results are displayed

Movies:
- movie list loads

Movie Detail:
- valid movie loads
- invalid movie is handled

Search:
- valid query works
- empty/no-result query behaves correctly

Genre:
- filter works

Surprise Me:
- returns a valid movie

Responsive UI:
- no obvious horizontal overflow
- cards remain usable

Interactions:
- hover effects behave correctly
- animations are smooth
- 3D movement is subtle
- links/buttons work

If browser automation or browser preview is available,
use it to visually inspect the page.

If screenshots can be captured,
inspect key pages visually.

If browser automation is unavailable,
perform HTTP smoke testing with Flask test client and/or curl
and clearly document the limitation.

==================================================
PHASE 12 — UI REVIEW
==================================================

After running the application, perform a UI review.

Check specifically that the final result does NOT appear overly AI-generated.

Ask:

- Is spacing consistent?
- Are effects restrained?
- Is gold used selectively?
- Is typography readable?
- Are cards aligned?
- Are posters visually dominant?
- Is glass used intentionally?
- Are shadows consistent?
- Are hover effects subtle?
- Does animation help rather than distract?
- Does the page feel cinematic?
- Does it look like one coherent product?

If the design feels excessively glossy, glowing, crowded,
or artificially futuristic:

reduce the effects.

Prefer restraint.

==================================================
PHASE 13 — BUG FIXING
==================================================

If any issue is discovered during testing:

1. Identify the root cause.
2. Fix the implementation.
3. Re-run the relevant test.
4. Re-run the full pytest suite.
5. Restart/test the application if necessary.

Do not merely describe bugs.

Fix them.

==================================================
PHASE 14 — REQUIREMENTS FILE
==================================================

Create or update requirements.txt.

It should contain only packages that are actually required.

Do not include Python standard-library modules.

Make sure a new environment can install dependencies with:

pip install -r requirements.txt

==================================================
PHASE 15 — RUN.MD
==================================================

This is mandatory.

After the application has been implemented and tested successfully,
create:

RUN.md

RUN.md must explain how another person can run the application
from a fresh clone.

Write RUN.md clearly enough for a beginner.

Include:

# MoodMovie — Run Guide

## 1. Requirements

Example:

- Python version
- pip
- supported OS assumptions if any

## 2. Open Project Directory

Example:

cd MOODMOVIE

## 3. Create Virtual Environment

Windows:

python -m venv venv

macOS/Linux:

python3 -m venv venv

## 4. Activate Virtual Environment

Windows CMD:

venv\Scripts\activate

Windows PowerShell:

.\venv\Scripts\Activate.ps1

macOS/Linux:

source venv/bin/activate

## 5. Install Dependencies

pip install -r requirements.txt

## 6. Initialize Database

Explain whether initialization happens automatically.

If a command is needed, document the exact command.

## 7. Run Tests

pytest

Include expected successful result.

## 8. Run Application

Example:

python app.py

or the actual command used.

## 9. Open Browser

Example:

http://127.0.0.1:5000

## 10. Main Pages / Features

Explain how to test:

- Mood selection
- Recommendations
- Movie list
- Search
- Genre filter
- Surprise Me
- Movie detail

## 11. Stop Application

Ctrl + C

## 12. Troubleshooting

Include common issues such as:

- Python not found
- pip dependencies missing
- port already in use
- virtual environment activation
- database recreation if needed

## 13. Project Structure Summary

Show a concise tree of the final project.

==================================================
PHASE 16 — FINAL VALIDATION
==================================================

Before considering the task complete, verify:

[ ] All four specification Markdown files were read
[ ] Existing specification documents were preserved
[ ] Project follows OOAD
[ ] Project follows OOP
[ ] Flask application works
[ ] HTML/CSS/JS load correctly
[ ] SQLite database works
[ ] Database contains demo movies
[ ] Mood recommendation works
[ ] Movie list works
[ ] Movie detail works
[ ] Search works
[ ] Genre filter works
[ ] Surprise Me works
[ ] Invalid routes/items handled
[ ] Responsive UI implemented
[ ] Dark cinematic theme implemented
[ ] Gold accent implemented
[ ] Glass UI implemented with restraint
[ ] Smooth animations implemented
[ ] 3D hover implemented with restraint
[ ] UI does not look excessively AI-generated
[ ] pytest suite passes
[ ] Application run test completed
[ ] requirements.txt is correct
[ ] RUN.md exists
[ ] RUN.md instructions were verified

==================================================
FINAL RESPONSE
==================================================

After completing everything, provide a concise engineering summary containing:

1. What was built
2. Final project architecture
3. Main classes
4. Main pages/routes
5. Database structure
6. Tests performed
7. Test result
8. UI validation result
9. How to run the project
10. Important files created

Do not only provide code snippets in the response.

Actually create and modify the project files in the workspace.

Continue until the project is in a runnable and tested 