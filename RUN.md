# MoodMovie — Run Guide

## 1. Requirements

- Python 3.10 or newer with pip and the venv module. Render is pinned to Python
  3.14.5 via `.python-version`. Tested on Windows with
  Python 3.14.5, Flask 3.1.3, SQLAlchemy 2.0.52, and pytest 9.1.1.
- A modern browser. Microsoft Edge was used for desktop and mobile emulation tests.
- Internet access to install packages initially. The finished app, posters, fonts,
  and database work offline. No API keys are needed.
- Commands below support Windows, macOS, and Linux; only Windows was executed here.

## 2. Open Project Directory

Open a terminal in the downloaded/cloned project folder containing `app.py`:

```text
cd MoodMovie
```

Use your actual folder location if needed. All subsequent commands run from that folder.

## 3. Create Virtual Environment

Windows:

```powershell
python -m venv .venv
```

macOS/Linux:

```bash
python3 -m venv .venv
```

If Windows opens the Microsoft Store or hangs on `python`, use a working Python
installation through `py -3 -m venv .venv`, or its full `python.exe` path. This
workspace had a broken WindowsApps alias; creating `.venv` with the installed
Python executable resolved it. Once created, use the virtual environment directly.

## 4. Activate Virtual Environment

Windows CMD:

```bat
.venv\Scripts\activate.bat
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Activation is optional. If PowerShell blocks activation, use the explicit commands
in section 8; you do not need to change your machine's execution policy.

## 5. Install Dependencies

With the environment activated:

```text
python -m pip install -r requirements.txt
```

Flask serves the app, SQLAlchemy accesses SQLite, and pytest runs the test suite.
Gunicorn serves production requests on Render/Linux; Waitress performs local
Windows WSGI verification. Direct dependency versions are pinned. SQLite itself
is included with Python. No Node tooling or Flask-SQLAlchemy extension is used.

## 6. Initialize Database

Initialization is automatic when the Flask app is created. The first run creates
`database/moodmovie.db` with `movies`, `moods`, and `genres` tables, then inserts
24 movies, six moods, and eight genres. Repeated startup does not duplicate movies.
Each film has one primary mood and one primary genre. Tests use temporary databases
and do not change your application database.

No manual database command is necessary. An optional `MOODMOVIE_DATABASE`
environment variable can specify a different SQLite file. Its parent directory
must be writable. Existing nonempty catalogs are preserved rather than reseeded.

## 7. Run Tests

```text
pytest
```

Or, to ensure you use the selected Python environment:

```text
python -m pytest
```

Expected result for this version: **63 passed**. Runtime varies by computer.
Tests cover model behavior, database integrity and seed initialization, repository
queries, services, recommendations, all routes, input validation, empty results,
an empty database, local assets, factory startup, restart preservation, and exact
Linux filename spelling for imports, templates, and rendered static references.

## 8. Run Application

With the environment activated:

```text
python app.py
```

Without activation, these are the exact commands verified in Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe app.py
```

On macOS/Linux without activation:

```bash
.venv/bin/python app.py
```

The terminal should display `Running on http://127.0.0.1:5000` with debug mode off.
Keep that terminal running. The bundled Flask server is intended for local class
demonstrations, not public production hosting.

## 9. Open Browser

Open [MoodMovie locally](http://127.0.0.1:5000).

## 10. Main Pages / Features

| Feature | How to try it |
|---|---|
| Home `/` | Select **Find my mood** to jump to the mood selector. |
| Recommendations `/recommend` | Click Happy, Sad, Romantic, Excited, Bored, or Relaxed; each returns four films, highest demo rating first. |
| All movies `/movies` | Open Movies; the collection contains 24 films. |
| Detail `/movie/13` | Click any film card; Interstellar shows its year, genre, duration, synopsis, mood, and rating. |
| Search `/search` | Search `Interstellar` or `wormhole`; try `zzzzzzz` for no results, or submit an empty query for guidance. |
| Genre `/genre/Sci-Fi` | Select Sci-Fi; three matching films appear. All movies resets the filter. |
| Surprise me `/random` | Receive a redirect to a randomly selected movie detail page. |
| Missing movie `/movie/999` | See a styled 404 with links back to discovery. |
| Responsive UI | Resize the browser; mobile uses a Menu button and two movie columns. |

Recommendations are simple curated rules, not predictions about the user. Scores
are fixed illustrative demo ratings. Posters are locally bundled vector
interpretations, not official theatrical posters. There is no login or streaming.

While the server is running, a second terminal can verify real HTTP behavior:

```text
python scripts/smoke_http.py
```

Expected: **19 real-server HTTP checks** pass. An alternate server URL can be passed
as an argument, for example `python scripts/smoke_http.py http://127.0.0.1:5001`.

Optional browser validation requires Microsoft Edge installed locally:

```text
python -m pip install -r requirements-browser.txt
python scripts/verify_browser.py
```

This runs headless Edge against port 5000 by default and writes screenshots and
`artifacts/browser-report.json`. It checks desktop/mobile interactions, five
viewport widths, keyboard access, image fallback, reduced motion, JavaScript
errors, and operation without JavaScript. Browser tooling is optional and is not
required to use the application or run pytest.

To validate the Windows production-style WSGI server, run this command from an
activated environment (the `--call` flag is required for this app factory):

```text
waitress-serve --call --listen=127.0.0.1:8000 app:create_app
```

Without activation in PowerShell, the exact tested command is:

```powershell
.\.venv\Scripts\waitress-serve.exe --call --listen=127.0.0.1:8000 app:create_app
```

Open `http://127.0.0.1:8000`, then run these checks in another terminal:

```powershell
.\.venv\Scripts\python.exe scripts/smoke_http.py http://127.0.0.1:8000
.\.venv\Scripts\python.exe scripts/verify_browser.py http://127.0.0.1:8000 artifacts/waitress
```

Expected: 19 HTTP checks and 10 browser check groups pass. The browser command
needs the optional browser requirements. Stop Waitress with Ctrl+C.

For a fresh database test without touching the usual database, set a new path
before starting Waitress in that same PowerShell terminal:

```powershell
$env:MOODMOVIE_DATABASE = Join-Path (Get-Location) ('artifacts/fresh-' + [guid]::NewGuid().ToString('N') + '/catalog.db')
.\.venv\Scripts\waitress-serve.exe --call --listen=127.0.0.1:8000 app:create_app
```

The nested directory and database are created on startup. After stopping the
server, `Remove-Item Env:MOODMOVIE_DATABASE` clears only the environment override.
The isolated test database stays in `artifacts/` for inspection.

## 11. Stop Application

Press **Ctrl+C** in the terminal running Flask. To leave an activated environment:

```text
deactivate
```

## 12. Troubleshooting

- **Python not found / Microsoft Store opens:** use a real Python installation
  and its launcher or executable path as described in section 3.
- **Missing Flask or SQLAlchemy:** reinstall with the same interpreter used to run
  the app, for example `.\.venv\Scripts\python.exe -m pip install -r requirements.txt`.
- **PowerShell activation blocked:** use `.\.venv\Scripts\python.exe` directly.
- **Port 5000 already in use:** stop the earlier Flask process, or choose port 5001.
  In PowerShell run `$env:PORT = "5001"` then `python app.py`; in CMD run
  `set PORT=5001` then `python app.py`; in macOS/Linux run `PORT=5001 python app.py`.
  Open `http://127.0.0.1:5001`. Pass that URL to the optional browser script.
- **`module 'app' has no attribute 'app'`:** use `app:create_app` with Waitress's
  `--call`, or `"app:create_app()"` with Gunicorn. `app:app` is not this project's
  entry point. Do not add a second module-level application to work around it.
- **Gunicorn errors about Unix-only modules on Windows:** run Waitress locally;
  the documented Gunicorn command is for Render/Linux.
- **Database locked:** stop other app instances or SQLite editors, then restart.
- **Need a fresh demo database:** stop Flask, back up/rename
  `database/moodmovie.db` to an unused name, then run `python app.py` again. The
  default catalog is recreated automatically. Keep the backup if it contains edits.
- **Posters missing:** the SVGs should be included under `static/images/posters`.
  Rebuild them using `python scripts/build_posters.py`. A local fallback handles
  an individual failed image when JavaScript is enabled; card links remain usable.
- **Browser test cannot launch Edge:** install Microsoft Edge or skip the optional
  browser checks. The app and pytest do not depend on a browser installation.

## 13. Project Structure Summary

```text
MoodMovie/
  app.py                    Flask factory and dependency composition
  config.py                 Portable paths and request limits
  requirements.txt          Application and pytest dependencies
  requirements-browser.txt  Optional Playwright dependency
  models/                   Movie, Mood, Genre ORM/domain classes
  database/                 DatabaseManager, seed data, generated SQLite file
  repositories/             MovieRepository queries
  services/                 MovieService and RecommendationEngine
  routes/                   Thin Flask controllers
  templates/                Jinja pages and reusable components
  static/                   CSS, vanilla JavaScript, local SVG artwork
  tests/                    63 pytest cases
  scripts/                  Poster builder, HTTP and browser verification
  artifacts/                Generated browser report and screenshots (ignored)
  IMPLEMENTATION_PLAN.md    Requirements analysis and implementation decisions
  VALIDATION.md             Final checklist and validation evidence
  READEAM.md                Original overview specification, name preserved
  MASTER_PROMPT.md           Original execution instructions
  MoodMovie_*.md            Original design, class, and use-case specifications
  RUN.md                    This guide
  render.yaml               Render Free Web Service blueprint
  .python-version           Render Python runtime pin
  DEPLOY_CHECKLIST.md        Deployment verification and remaining hosted checks
```

# Deploy to Render

## Prerequisites

- A GitHub repository containing this project and a Render account with access
  to that repository.
- Branch `main`. This workspace's Git root is the MoodMovie folder itself;
  `app.py`, `requirements.txt`, `.python-version`, and `render.yaml` are at its root.
- Run the tests and Waitress checks above before pushing changes.

## Push to GitHub

Review `git status` and confirm `origin` points to your GitHub repository, then:

```text
git add .
git commit -m "Prepare MoodMovie for Render deployment"
git push origin main
```

The preparation process does not push or create a hosted service automatically.
`.gitignore` excludes local environments, secrets, databases, caches, and artifacts.
Commit the source, local posters, tests, and new deployment configuration.

## Create Web Service

In Render, select **New → Web Service → Connect GitHub repository** and choose
the repository containing MoodMovie. Use the settings below. Alternatively,
**New → Blueprint** can use the included `render.yaml`; it describes the same
Free Python service. Choose one creation method to avoid duplicate services.

## Render Settings

| Setting | Exact value |
|---|---|
| Name | `moodmovie` |
| Runtime | Python 3 |
| Branch | `main` |
| Root Directory | **Leave blank** (repository root; do not enter `MoodMovie`) |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 4 "app:create_app()"` |
| Health Check Path | `/` |
| Plan / Instance Type | Free |
| Auto Deploy | Yes / On Commit (`autoDeployTrigger: commit` in the blueprint) |
| Python version | `3.14.5`, supplied by the committed `.python-version` |

No user-supplied environment variables or secrets are required. Render supplies
`PORT`; Gunicorn binds to `0.0.0.0` on that port. Do not use the Flask development
server as Render's Start Command. [Render port binding documentation](https://render.com/docs/web-services#port-binding).

The entry point is verified from the actual source: `app.py` defines
`create_app(test_config=None)`, which constructs Flask, initializes the database,
composes services/repository, registers blueprints, and returns the WSGI app.
Gunicorn calls this factory with no arguments. `app.run()` is protected by
`if __name__ == "__main__"` and is never used by the production server.

One worker keeps first-run schema/seed creation in a single process. Four threads
allow concurrent requests; each repository operation opens its own SQLAlchemy
session. Keep this worker setting for the current mini-project initialization
design. The application explicitly defaults to debug off.

There is no session/login feature, so `SECRET_KEY` is not used or needed.
`MOODMOVIE_DATABASE` is an optional filesystem override for local tests; leave it
unset on Render to use the portable default. `.python-version` avoids relying
on a changing platform default. Remove any conflicting `PYTHON_VERSION` override
from an existing service. [Render Python version settings](https://render.com/docs/python-version).

The blueprint omits `rootDir` deliberately because the app is at the Git root.
Its keys were checked against the [Render Blueprint specification](https://render.com/docs/blueprint-spec).

## Deployment

Select **Create Web Service** and watch the build/deploy logs. The build installs
the pinned direct dependencies; startup should load the factory and initialize
the demo database without manual commands. Wait for the service to report healthy,
then open the actual `onrender.com` URL shown in Render. Do not assume that the
requested service name determines an available public URL.

Subsequent commits to `main` trigger deployment when Auto Deploy is enabled.
An existing service can also deploy the latest commit from the dashboard.

## Verify

On the hosted URL, verify:

- `/`: page, six mood buttons, posters, CSS, and JavaScript load.
- Select each mood: four recommendations appear, sorted by demo rating.
- `/movies`: 24 films appear.
- `/movie/13`: Interstellar details load; `/movie/999` returns the styled 404.
- `/search?q=Interstellar`: one result; empty and no-result searches remain usable.
- `/genre/Sci-Fi`: three films appear.
- `/random`: redirects to a valid film detail page.

After the service has woken up, the HTTP script can check its actual public URL:

```text
python scripts/smoke_http.py https://YOUR-ACTUAL-SERVICE.onrender.com
```

Replace the example hostname. Local verification has passed; an actual hosted
deployment and these public-URL checks have not been performed during preparation.
The Linux Gunicorn command was validated against the factory and installed
Gunicorn source, not executed natively on Windows.

## Cold Start Note

Render Free services spin down after inactivity; the next request can take longer
while the service wakes up. The current documentation specifies 15 minutes idle
and roughly a minute to restart. [Render Free service behavior](https://render.com/docs/free#spinning-down-on-idle).

## SQLite Note

Runtime SQLite persistence on Render Free is not guaranteed. Files can be lost
on restart, redeployment, or spin-down. [Render ephemeral filesystem behavior](https://render.com/docs/free#local-files-lost-on-redeploy).

MoodMovie recreates its database directory and tables automatically and seeds
24 films, six moods, and eight genres when the movie table is empty. Repeated
startup preserves a nonempty catalog without duplicate seeds. The shipped UI
only reads curated data, so it does not depend on persistent user submissions.
Any manual database edits on Render can be lost; edit the seed source and redeploy
for reproducible demo content. No persistent disk is required for this demo.
