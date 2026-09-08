# MoodMovie — Run Guide

## 1. Requirements

- Python 3.10 or newer with pip and the venv module. Tested on Windows with
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
SQLite itself is included with Python. No Node tooling is used.

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

Expected result for this version: **57 passed**. Runtime varies by computer.
Tests cover model behavior, database integrity and seed initialization, repository
queries, services, recommendations, all routes, input validation, empty results,
an empty database, and local assets.

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

This runs headless Edge against port 5000 and writes screenshots and
`artifacts/browser-report.json`. It checks desktop/mobile interactions, five
viewport widths, keyboard access, image fallback, reduced motion, JavaScript
errors, and operation without JavaScript. Browser tooling is optional and is not
required to use the application or run pytest.

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
  Open `http://127.0.0.1:5001`. The optional browser script expects port 5000.
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
  tests/                    57 pytest cases
  scripts/                  Poster builder, HTTP and browser verification
  artifacts/                Generated browser report and screenshots (ignored)
  IMPLEMENTATION_PLAN.md    Requirements analysis and implementation decisions
  VALIDATION.md             Final checklist and validation evidence
  READEAM.md                Original overview specification, name preserved
  MASTER_PROMPT.md           Original execution instructions
  MoodMovie_*.md            Original design, class, and use-case specifications
  RUN.md                    This guide
```
