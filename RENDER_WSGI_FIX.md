# MoodMovie — Render WSGI Fix & Production Readiness

You are responsible for fixing the current Render deployment failure of the existing MoodMovie Flask project.

Do NOT rebuild the project from scratch.

Do NOT redesign working parts unnecessarily.

Preserve the current OOAD/OOP architecture and make the minimum clean production-safe changes required.

==================================================
CURRENT DEPLOYMENT STATUS
==================================================

Render successfully completed the build:

Build successful 🎉

Dependencies installed successfully, including:

- Flask
- SQLAlchemy
- pytest
- gunicorn
- waitress

However, deployment failed during application startup.

Render currently executes:

gunicorn app:app

and returns:

AttributeError:
module 'app' has no attribute 'app'

Gunicorn then reports:

Failed to find attribute 'app' in 'app'

A similar local Waitress test on Windows also failed:

waitress-serve --listen=127.0.0.1:8000 app:app

with:

module 'app' has no attribute 'app'

This strongly suggests that the application does not expose a module-level:

app = Flask(...)

and may instead use an application factory such as:

def create_app():
    ...

Do NOT assume this.

Inspect the actual code first.

==================================================
PRIMARY OBJECTIVE
==================================================

Fix the WSGI entry point and prepare MoodMovie so that:

1. It can run locally on Windows using Waitress.
2. It can run on Render Linux using Gunicorn.
3. The existing Flask application architecture remains clean.
4. Automated tests still pass.
5. SQLite initialization still works.
6. Existing routes/templates/static assets still work.
7. Render has one clear production Start Command.
8. RUN.md documents the actual deployment configuration.

==================================================
PHASE 1 — INSPECT ACTUAL FLASK ARCHITECTURE
==================================================

Inspect:

- app.py
- config.py
- routes/
- services/
- repositories/
- models/
- database/
- requirements.txt
- RUN.md
- render.yaml if present
- tests/

Determine exactly how the Flask app is created.

Check whether app.py contains:

A)

app = Flask(__name__)

or:

B)

def create_app():
    ...

or another application setup.

Run appropriate inspection commands.

For example:

python -c "import app; print('FILE:', app.__file__); print('has app:', hasattr(app, 'app')); print('has create_app:', hasattr(app, 'create_app')); print([x for x in dir(app) if not x.startswith('_')])"

If create_app exists, verify it:

python -c "from app import create_app; application=create_app(); print(application); print(application.url_map)"

Do not modify code until the architecture is understood.

==================================================
PHASE 2 — CHOOSE THE CLEANEST WSGI STRATEGY
==================================================

Use the existing architecture to determine the best production entry point.

If the project intentionally uses an application factory, prefer preserving it.

Recommended solution for an application factory:

Create a production WSGI entry point:

wsgi.py

with:

from app import create_app

app = create_app()

Then production servers can use:

wsgi:app

This provides a simple and explicit production entry point.

However:

Do NOT create wsgi.py blindly.

First verify that:

from app import create_app

is actually correct.

If create_app lives in another module, use the correct import.

If the current project already has a valid WSGI entry file, reuse it instead of creating duplicates.

==================================================
PHASE 3 — IMPLEMENT WSGI ENTRY POINT
==================================================

If the application factory structure is confirmed, create or update:

wsgi.py

The file should contain only what is required to expose the Flask WSGI application.

Expected concept:

from app import create_app

app = create_app()

Avoid:

- debug mode
- app.run()
- development-only logic
- duplicate route registration
- duplicate database initialization

wsgi.py should be a clean production entry point.

==================================================
PHASE 4 — VERIFY PYTHON IMPORT
==================================================

After implementing the WSGI entry point, verify it directly.

Run:

python -c "from wsgi import app; print(app); print(app.url_map)"

The import must succeed without exceptions.

Verify that the URL map includes the existing main routes, such as:

/
recommendation route
/movies
movie detail
search
genre
random

Use the actual project route names.

If routes are missing, investigate and fix the root cause.

==================================================
PHASE 5 — WINDOWS WSGI TEST
==================================================

Because development is currently on Windows, use Waitress for local WSGI verification.

If wsgi.py exposes:

app

test with:

waitress-serve --listen=127.0.0.1:8000 wsgi:app

Start the application and verify that it responds.

At minimum verify:

GET /
GET /movies
movie detail route
search route
genre filter
random movie

Also test mood recommendation using its correct HTTP method.

Verify:

- HTML renders
- CSS loads
- JavaScript loads
- images/fallbacks load
- no server exceptions occur

If browser automation is available, visually inspect the website.

Otherwise use Flask test client, HTTP requests, curl, or equivalent smoke testing.

==================================================
PHASE 6 — DETERMINE RENDER START COMMAND
==================================================

After successful WSGI verification, determine the exact Render Start Command.

If using:

wsgi.py

with module-level:

app

the expected Render command is:

gunicorn wsgi:app

Use this ONLY if verified.

Do not leave Render documentation using:

gunicorn app:app

if app.py does not expose app.

If the architecture requires another import path, document the actual verified path.

==================================================
PHASE 7 — REQUIREMENTS REVIEW
==================================================

Inspect requirements.txt.

Confirm Gunicorn is included.

Confirm Waitress is available for Windows local production-style testing if the project intends to document it.

Keep only required dependencies.

Do not use pip freeze blindly.

Current dependencies may include:

Flask
SQLAlchemy
pytest
gunicorn
waitress

Retain versions only if they are compatible and intentionally pinned.

==================================================
PHASE 8 — PYTHON VERSION REVIEW
==================================================

Render currently reported:

Python 3.14.5

Inspect:

.python-version

if present.

Also determine the Python version used locally.

Run:

python --version

Consider whether the project should pin the same tested Python version on Render.

Do not change Python version without a reason.

If the project was developed and tested on a stable version such as Python 3.12 or 3.13, consider aligning Render with that tested version.

If Python 3.14 is already fully working with all project dependencies and tests, it may remain.

Document the decision.

==================================================
PHASE 9 — SQLITE STARTUP SAFETY
==================================================

Verify that calling:

create_app()

through Gunicorn/Waitress does not cause unsafe or duplicate database behavior.

Confirm:

- database directory exists or is created safely
- tables initialize automatically when required
- seed data initializes only when database is empty
- repeated application startups do not duplicate movie records
- startup does not rely on Windows-specific paths
- SQLite path works on Linux

Do not redesign SQLite unless a real problem exists.

Remember that Render Free filesystem persistence is not guaranteed.

The core MoodMovie demo must remain functional after database recreation.

==================================================
PHASE 10 — PRODUCTION-SAFE APP STARTUP
==================================================

Inspect app.py.

If it contains:

if __name__ == "__main__":
    ...

keep development startup separated from production.

For example, application factory architecture may remain conceptually:

def create_app():
    ...
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(...)

This is acceptable for local development.

Gunicorn must use the WSGI entry point instead.

Ensure production deployment does not depend on app.run().

Debug mode must not be enabled in production.

==================================================
PHASE 11 — TEST EVERYTHING
==================================================

Run:

pytest

Fix any failures caused by the deployment changes.

Do not modify tests merely to hide real failures.

After fixes, run the full suite again.

All tests should pass.

Then perform an application smoke test through Waitress.

==================================================
PHASE 12 — STATIC FILE AND LINUX REVIEW
==================================================

Because Render uses Linux, inspect case sensitivity carefully.

Check all references to:

templates/
static/
static/css/
static/js/
static/images/

Ensure file names and references match exactly.

Examples:

style.css != Style.css
main.js != Main.js

Fix any case mismatches.

Check for Windows-only path separators or absolute paths.

==================================================
PHASE 13 — UPDATE RENDER CONFIGURATION
==================================================

Update documentation and configuration to use the actual verified settings.

Expected configuration if wsgi.py is used:

Runtime:
Python 3

Build Command:
pip install -r requirements.txt

Start Command:
gunicorn wsgi:app

Health Check Path:
/

Branch:
main

Auto Deploy:
Yes

Root Directory:
determine from actual repository structure

Do NOT guess Root Directory.

Inspect the repository.

==================================================
PHASE 14 — RENDER.YAML
==================================================

If render.yaml already exists, inspect and correct it.

If it contains:

startCommand: gunicorn app:app

replace it with the verified command.

For example:

startCommand: gunicorn wsgi:app

Only if this matches the actual working architecture.

If render.yaml does not exist, do not create it unless it improves deployment reproducibility.

==================================================
PHASE 15 — UPDATE RUN.MD
==================================================

Update RUN.md so that it accurately reflects the finished project.

Add or correct:

## Local Development

Example:

python app.py

or the actual development command.

## Windows Production-style Test

Document the verified Waitress command.

Expected if wsgi.py is used:

waitress-serve --listen=127.0.0.1:8000 wsgi:app

## Render Deployment

Document:

Build Command:
pip install -r requirements.txt

Start Command:
gunicorn wsgi:app

Use the actual verified command.

Also explain why:

gunicorn app:app

is not correct for this architecture.

Keep the explanation concise.

==================================================
PHASE 16 — DEPLOYMENT CHECKLIST
==================================================

Update or create:

DEPLOY_CHECKLIST.md

Include:

[ ] Flask application factory verified
[ ] WSGI module imports successfully
[ ] wsgi.py exposes app
[ ] URL map loads
[ ] Waitress local WSGI test passes
[ ] pytest passes
[ ] Gunicorn included in requirements.txt
[ ] Render Start Command verified
[ ] no hardcoded Windows paths
[ ] SQLite initializes safely
[ ] seed data does not duplicate
[ ] templates load
[ ] CSS loads
[ ] JavaScript loads
[ ] Linux filename casing checked
[ ] debug disabled in production
[ ] RUN.md updated
[ ] render.yaml updated if present

==================================================
PHASE 17 — GIT DIFF REVIEW
==================================================

Before completing the task, inspect all changes.

Use git diff or equivalent.

Confirm that changes are minimal and intentional.

Do not leave:

- debug print statements
- temporary scripts
- test artifacts
- accidental database corruption
- unnecessary generated files

==================================================
PHASE 18 — FINAL VERIFICATION
==================================================

Perform final verification in this order:

1. Import app architecture.
2. Import WSGI application.
3. Run pytest.
4. Run Waitress locally.
5. Test major routes.
6. Stop Waitress cleanly.
7. Review requirements.txt.
8. Review RUN.md.
9. Review Render configuration.
10. Review git diff.

Do not claim success unless the project passes these checks.

==================================================
FINAL OUTPUT
==================================================

At the end, clearly report:

DETECTED FLASK ARCHITECTURE:
<actual result>

WSGI ENTRY FILE:
<actual file>

LOCAL WINDOWS WSGI COMMAND:
<actual verified command>

RENDER BUILD COMMAND:
<actual command>

RENDER START COMMAND:
<actual verified command>

ROOT DIRECTORY:
<actual setting>

PYTHON VERSION:
<actual/recommended version>

PYTEST RESULT:
<number passed / failed>

LOCAL WSGI TEST:
PASS / FAIL

SQLITE STARTUP TEST:
PASS / FAIL

FILES CREATED:
<list>

FILES MODIFIED:
<list>

DEPLOYMENT STATUS:
READY / NOT READY

If READY, explicitly state:

"The project is ready to push to GitHub and redeploy on Render."

Do not stop after explaining the fix.

Actually inspect, modify, test, and verify the project.