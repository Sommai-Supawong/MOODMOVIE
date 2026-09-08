You are preparing the existing MoodMovie Flask project for deployment to Render.

Do not redesign the whole project.
Do not replace the current architecture unnecessarily.

Your job is to inspect the existing project, determine the real Flask application entry point, prepare the project for production deployment on Render, verify it locally as much as possible, and document the exact deployment settings.

==================================================
PRIMARY GOAL
==================================================

Prepare the existing MoodMovie project so it can be deployed reliably to Render Free Web Service.

The project currently runs on Windows during development.

A previous production-server test using:

waitress-serve --listen=127.0.0.1:8000 app:app

failed with:

module 'app' has no attribute 'app'

This strongly suggests the project may use a Flask application factory such as:

create_app()

Do NOT assume the production start command.

Inspect the actual project and determine it from the code.

==================================================
STEP 1 — INSPECT THE PROJECT
==================================================

Inspect the current workspace.

Read the relevant files, especially:

- app.py
- config.py
- requirements.txt
- routes/
- services/
- repositories/
- database/
- tests/
- RUN.md if it already exists
- README.md

Also inspect the Flask initialization code.

Determine whether the project uses:

A. module-level Flask app:

app = Flask(__name__)

or

B. application factory:

def create_app():
    ...

or another structure.

Report the detected structure before making changes.

==================================================
STEP 2 — DETERMINE THE CORRECT WSGI ENTRY POINT
==================================================

Determine the correct production WSGI entry point.

Examples:

If app.py contains:

app = Flask(__name__)

then the likely entry point is:

app:app

If app.py contains:

def create_app():
    ...

then the likely entry point is:

app:create_app()

Do not guess.

Verify the correct import path using Python.

Examples of acceptable verification:

python -c "import app; print(app.__file__); print(dir(app))"

and, if using application factory:

python -c "from app import create_app; application=create_app(); print(application); print(application.url_map)"

If the current structure makes production deployment awkward, make the smallest safe change necessary.

Do not break the existing OOAD/OOP architecture.

==================================================
STEP 3 — WINDOWS LOCAL PRODUCTION TEST
==================================================

Because Gunicorn does not run natively on Windows, use Waitress for local WSGI verification.

If the project exposes a module-level app:

waitress-serve --listen=127.0.0.1:8000 app:app

If the project uses create_app():

waitress-serve --call --listen=127.0.0.1:8000 app:create_app

Use the correct command based on the actual project.

Start the server and verify:

- homepage loads
- static CSS loads
- JavaScript loads
- mood recommendation works
- movies page works
- movie detail works
- search works
- genre filter works
- random movie works

If browser automation is available, inspect the application visually.

If browser automation is unavailable, use HTTP smoke tests or Flask test client.

==================================================
STEP 4 — PREPARE REQUIREMENTS.TXT
==================================================

Inspect requirements.txt.

Ensure all packages required by the finished project are listed.

At minimum, include only if actually used:

Flask
gunicorn
waitress
pytest

Include Flask-SQLAlchemy only if the project actually uses it.

Do not add unnecessary packages.

Do not use pip freeze blindly if it would include unrelated environment packages.

The requirements file should be minimal and reproducible.

==================================================
STEP 5 — PREPARE GUNICORN FOR RENDER
==================================================

Render will run on Linux.

Ensure Gunicorn is included in requirements.txt.

Determine the exact Render Start Command based on the real app structure.

Examples:

Module-level app:

gunicorn app:app

Application factory:

gunicorn "app:create_app()"

If the actual import path is different, use the correct real path.

Do not document a command that has not been verified logically from the code.

==================================================
STEP 6 — PRODUCTION CONFIGURATION
==================================================

Inspect the Flask configuration.

Ensure production deployment does not depend on:

- hardcoded Windows paths
- D:\ paths
- debug=True
- local-only filesystem assumptions
- development server behavior
- machine-specific environment variables

Use portable paths.

Prefer pathlib or os.path based on the project structure.

Make sure:

debug mode is disabled in production.

If app.py contains:

app.run(debug=True)

that is acceptable only inside:

if __name__ == "__main__":

because Gunicorn should not execute the Flask development server.

==================================================
STEP 7 — PORT / HOST COMPATIBILITY
==================================================

Render provides networking for the web service.

When using Gunicorn, do not rely on app.run() for production.

Do not hardcode a production port.

If the project has any code that requires PORT, use:

os.environ.get("PORT")

only where appropriate.

Do not unnecessarily complicate the project.

==================================================
STEP 8 — SQLITE DEPLOYMENT REVIEW
==================================================

The current project uses SQLite.

Review the project to ensure the core demo can survive Render's ephemeral filesystem behavior.

For this MoodMovie mini project:

- database initialization should happen automatically if needed
- tables should be created automatically
- demo seed data should be created automatically if the database is empty
- core application behavior must not depend on persistent user-generated data

Do not create duplicate seed records on every startup.

Use safe initialization logic such as:

if tables/database are empty:
    seed data

Verify a fresh environment can start without manually creating the database.

==================================================
STEP 9 — STATIC FILES AND TEMPLATES
==================================================

Verify all template and static paths are portable.

Check:

templates/
static/css/
static/js/
static/images/

Ensure Flask can find them in production.

Inspect for:

- Windows absolute paths
- local filesystem references
- broken image references
- incorrect case sensitivity

Important:

Render uses Linux, so filename case matters.

Example:

style.css

is different from:

Style.css

on Linux.

Fix case-sensitivity issues if any.

==================================================
STEP 10 — ENVIRONMENT VARIABLES
==================================================

Determine whether the project needs environment variables.

If not required, do not invent unnecessary ones.

If SECRET_KEY is used, support reading it from environment:

SECRET_KEY

Provide a safe development fallback only if appropriate.

Do not commit real secrets.

Create or update .gitignore to exclude:

.env
.venv/
__pycache__/
*.pyc
pytest cache
local temporary files

Do not ignore source files required for deployment.

==================================================
STEP 11 — DATABASE PATH SAFETY
==================================================

Review the SQLite database path.

It must not use a Windows-specific absolute path.

Use a project-relative or instance-relative path.

Example concept:

PROJECT_ROOT / "database" / "moodmovie.db"

or Flask instance folder if the current design supports it.

Make sure directories are created safely before SQLite tries to use them.

==================================================
STEP 12 — TEST SUITE
==================================================

Run the existing automated tests.

Use:

pytest

Fix any failing tests caused by deployment preparation.

Then re-run the full test suite.

All tests should pass before proceeding.

If tests currently depend on the production database, improve them to use an isolated test database where reasonable.

Do not break functional behavior just to make tests pass.

==================================================
STEP 13 — FRESH-START TEST
==================================================

Simulate a fresh deployment as closely as possible.

Verify the application works without relying on:

- an already-created local database
- cached files
- previous runtime state

If safe, test database recreation using a temporary or test database.

Do not destroy important source data accidentally.

Verify:

startup
database initialization
seed data
homepage
recommendation flow

==================================================
STEP 14 — RENDER CONFIGURATION
==================================================

After inspection and testing, determine and document the exact Render settings.

Provide:

Name:
moodmovie

Runtime:
Python 3

Branch:
main

Root Directory:
determine based on actual repository structure

Build Command:
pip install -r requirements.txt

Start Command:
DETERMINE FROM ACTUAL PROJECT

Health Check Path:
/

Plan:
Free

Auto Deploy:
Yes

Do not assume Root Directory is blank.
Inspect the actual repository structure.

==================================================
STEP 15 — OPTIONAL RENDER.YAML
==================================================

If it improves reproducibility without adding unnecessary complexity, create:

render.yaml

Example structure:

services:
  - type: web
    name: moodmovie
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: <actual command>

Only create it if it matches the actual project structure.

Do not add unsupported or unnecessary configuration.

==================================================
STEP 16 — UPDATE RUN.MD
==================================================

Update RUN.md with a new section:

# Deploy to Render

Include:

## Prerequisites

- GitHub repository
- Render account

## Push to GitHub

Document:

git add .
git commit -m "Prepare MoodMovie for Render deployment"
git push origin main

## Create Web Service

Explain:

Render
→ New
→ Web Service
→ Connect GitHub repository

## Render Settings

Write the exact values discovered from this project:

Runtime
Root Directory
Build Command
Start Command
Health Check Path
Plan

## Deployment

Explain how to deploy.

## Verify

Test:

/
recommendation
/movies
movie detail
search
genre
random

## Cold Start Note

Mention that Render Free services may sleep when inactive and the first request can take longer.

## SQLite Note

Explain that SQLite runtime persistence on Render Free is not guaranteed.

Clarify that MoodMovie automatically initializes and seeds its demo data.

==================================================
STEP 17 — CREATE DEPLOYMENT CHECKLIST
==================================================

Create a concise deployment checklist either in RUN.md or a new file:

DEPLOY_CHECKLIST.md

Include:

[ ] app entry point verified
[ ] requirements.txt contains gunicorn
[ ] waitress local WSGI test passed
[ ] pytest passes
[ ] no absolute Windows paths
[ ] debug disabled for production
[ ] templates load
[ ] static CSS loads
[ ] JavaScript loads
[ ] SQLite initializes automatically
[ ] seed data initializes safely
[ ] no duplicate seeds
[ ] Linux filename casing checked
[ ] .gitignore correct
[ ] Render build command verified
[ ] Render start command verified
[ ] RUN.md updated

==================================================
STEP 18 — FINAL VERIFICATION
==================================================

Before finishing:

1. Run pytest again.
2. Verify the Flask application imports successfully.
3. Verify the WSGI entry point.
4. Verify local Waitress startup on Windows.
5. Verify key routes.
6. Verify fresh database initialization.
7. Verify requirements.txt.
8. Verify RUN.md.
9. Verify Render configuration.

Do not claim deployment readiness if a known error remains.

==================================================
IMPORTANT CONSTRAINTS
==================================================

- Preserve the existing OOAD/OOP structure.
- Do not rewrite the entire application.
- Make the minimum clean changes required for Render readiness.
- Do not replace Flask.
- Do not replace SQLite unless there is a true blocking reason.
- Do not introduce Docker unless necessary.
- Do not introduce React, Node, or frontend build tooling.
- Do not remove tests.
- Do not remove existing project documentation.
- Do not silently ignore errors.
- Fix issues you discover.

==================================================
FINAL RESPONSE
==================================================

When finished, report:

1. Detected Flask architecture
2. Correct WSGI entry point
3. Correct local Waitress command
4. Correct Render Start Command
5. Correct Render Build Command
6. Root Directory setting
7. Files modified
8. Tests run
9. Test results
10. Local production-server verification result
11. SQLite deployment behavior
12. Any remaining limitations

Most importantly, clearly print:

RENDER BUILD COMMAND:
<command>

RENDER START COMMAND:
<command>

LOCAL WINDOWS WSGI TEST COMMAND:
<command>

Then confirm whether the project is ready to deploy to Render.