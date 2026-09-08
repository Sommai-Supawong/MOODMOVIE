# MoodMovie Render deployment checklist

**Preparation status: READY.** This means locally verified and prepared to deploy;
no Render service was created and no public deployment was claimed.

## Detected architecture and plan

`RENDER_PREP.md` was read completely before changes. Inspection found the
application factory `app.create_app(test_config=None)` and no module-level `app`.
The previous `app:app` command was therefore invalid. The factory was imported
and called successfully before modifying files. The repository root contains
`app.py` and `requirements.txt`, and its current branch is `main`.

The pre-change plan was: add production-server dependencies/configuration;
preserve the OOAD/OOP layers; verify isolated fresh/repeated startup and filename
case; test through Waitress and a browser; document exact settings and evidence.
The existing 57-test baseline passed before modifications.

## Exact deployment settings

| Setting | Value |
|---|---|
| Name | `moodmovie` |
| Runtime | Python 3; `.python-version` pins `3.14.5` |
| Branch | `main` |
| Root Directory | **Leave blank**, using the inspected Git repository root |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 4 "app:create_app()"` |
| Health Check Path | `/` |
| Plan | Free |
| Auto Deploy | Yes / On Commit |
| Required custom environment variables | None; Render supplies `PORT` |

Windows WSGI command, in an activated virtual environment:

```text
waitress-serve --call --listen=127.0.0.1:8000 app:create_app
```

Exact PowerShell invocation used without activation:

```powershell
.\.venv\Scripts\waitress-serve.exe --call --listen=127.0.0.1:8000 app:create_app
```

## Completed checks

- [x] App entry point verified by actual Python import and factory call.
- [x] requirements.txt contains Gunicorn and Waitress; actual direct dependencies pinned.
- [x] Waitress local WSGI startup and request tests passed on Windows.
- [x] pytest passes: **63 tests**, including six deployment-specific tests.
- [x] No hardcoded absolute Windows paths in application code, templates, or static URLs.
- [x] Debug explicitly disabled by default; development server remains main-guarded.
- [x] Templates compile/render and all referenced names match exact filename case.
- [x] Static CSS loads through the actual WSGI server.
- [x] JavaScript loads; browser reports no JavaScript errors.
- [x] All 24 local posters, fallback image, and favicon resolve.
- [x] SQLite initializes automatically in a new nested directory.
- [x] Fresh database has 24 movies, six moods, and eight genres.
- [x] Repeated factory startup preserves data; no duplicate seeds.
- [x] Empty movie table reseeds safely while existing moods/genres remain unique.
- [x] Linux filename casing checked for local imports, templates, and static references.
- [x] .gitignore excludes secrets, environments, caches, local DBs, logs, and artifacts.
- [x] Deployment source, templates, posters, and configuration are not ignored.
- [x] Render build command installs in a separate clean Windows virtual environment.
- [x] Render start command verified logically from factory and installed Gunicorn source.
- [x] render.yaml uses documented fields and matches RUN.md settings.
- [x] RUN.md updated with Windows WSGI and real Render instructions.
- [x] Full suite rerun in the clean environment after changes.

## Verification evidence

| Check | Result |
|---|---|
| Existing pytest baseline | 57 passed |
| Updated full pytest suite | 63 passed |
| Clean virtual environment build | `pip install -r requirements.txt` succeeded |
| Clean virtual environment tests | 63 passed |
| Dependency check | No broken requirements |
| Actual Waitress HTTP smoke test | 19 checks passed at `http://127.0.0.1:8000` |
| Actual Waitress browser test | 10 groups passed in headless Microsoft Edge; zero JavaScript errors |
| Responsive browser checks | Six page types at 320, 390, 768, 1024, 1440 px; no overflow |
| Fresh live WSGI database | Automatically created, then independently counted using sqlite3 |
| Clean factory import | Flask WSGI app returned, debug off, 24 films initialized |
| Git whitespace validation | `git diff --check` passed |

The Waitress database was created under the isolated, ignored directory
`artifacts/render-wsgi-25214797de0242948c82504100589684/`. The ordinary
`database/moodmovie.db` was not deleted or replaced. A separate clean environment
was created in `artifacts/render-build-env/`; it has only project requirements,
not the optional browser package. Browser screenshots and the report are in
`artifacts/waitress/`. The desktop home screenshot was visually inspected.

The Gunicorn `import_app` implementation accepts a function call expression,
imports its module, and invokes the named factory. Its documented/source options
support `--bind`, `--workers`, and `--threads`. One worker avoids competing
first-run seed initialization; threads use existing per-operation database sessions.
Gunicorn itself was not launched natively on Windows and no Docker setup was added.

## Files changed

- `requirements.txt`: pins Flask/SQLAlchemy/pytest and includes Gunicorn/Waitress.
- `config.py`: explicit debug-off default and resolved portable default DB path.
- `.gitignore`: environment files, logs, and temporary-file exclusions.
- `.python-version`, `render.yaml`: reproducible runtime and Render service settings.
- `tests/test_deployment.py`: startup, persistence, safe reseeding, and case checks.
- `scripts/verify_browser.py`: accepts server URL and output directory so the
  same UI suite tests Waitress without altering application behavior.
- `RUN.md`, `DEPLOY_CHECKLIST.md`: exact commands, settings, evidence, and limitations.

The Flask factory, models, routes, services, repositories, database logic, and
UI were preserved. No secrets, account system, ORM replacement, or deployment-only
application wrapper was introduced. Original specification documents are untouched;
the overview is still named `READEAM.md` as supplied.

## Hosted verification still to perform

- [ ] Commit and push these changes to the GitHub `main` branch.
- [ ] Create the Render service using the documented settings or blueprint.
- [ ] Confirm Linux Gunicorn startup and the `/` health check in Render logs.
- [ ] Verify all discovery flows using the assigned public URL.

These steps require an actual deployment and are not represented as completed.
No known local application errors remain. Render Free may sleep when idle and
its runtime filesystem is ephemeral. MoodMovie restores its curated demo catalog
automatically and has no persistent user-generated data. Browser checks used
Edge emulation, not physical devices or every browser engine.

Platform references: [Render Flask deployment](https://render.com/docs/deploy-flask),
[port binding](https://render.com/docs/web-services#port-binding),
[Blueprint specification](https://render.com/docs/blueprint-spec),
[Python runtime selection](https://render.com/docs/python-version),
[Free service limits](https://render.com/docs/free), and
[Waitress factory CLI](https://docs.pylonsproject.org/projects/waitress/en/latest/runner.html).
