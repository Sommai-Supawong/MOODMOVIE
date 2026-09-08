# MoodMovie Render deployment checklist

**Preparation status: READY.** The reported Render startup failure is addressed
locally by an explicit WSGI module. Hosted settings/redeployment remain to be applied;
no successful public deployment is claimed.

## Detected architecture and plan

`RENDER_WSGI_FIX.md` was read completely before this fix. Inspection confirmed the
application factory `app.create_app(test_config=None)` and no module-level `app`.
The previous `app:app` command was therefore invalid. The factory was imported
and called successfully before modifying files. The repository root contains
`app.py` and `requirements.txt`, and its current branch is `main`.

The plan was to preserve the factory, expose its result in `wsgi.py`, update both
server entry points, test fresh WSGI imports and existing functionality, verify
Waitress/browser behavior, then review documentation and the final diff.

## Exact deployment settings

| Setting | Value |
|---|---|
| Name | `moodmovie` |
| Runtime | Python 3; `.python-version` pins `3.14.5` |
| Branch | `main` |
| Root Directory | **Leave blank**, using the inspected Git repository root |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 4 wsgi:app` |
| Health Check Path | `/` |
| Plan | Free |
| Auto Deploy | Yes / On Commit |
| Required custom environment variables | None; Render supplies `PORT` |

Windows WSGI command, in an activated virtual environment:

```text
waitress-serve --listen=127.0.0.1:8000 wsgi:app
```

Exact PowerShell invocation used without activation:

```powershell
.\.venv\Scripts\waitress-serve.exe --listen=127.0.0.1:8000 wsgi:app
```

## Completed checks

- [x] App entry point verified by actual Python import and factory call.
- [x] `wsgi.py` exposes `app`; direct WSGI import succeeds and the URL map loads.
- [x] requirements.txt contains Gunicorn and Waitress; actual direct dependencies pinned.
- [x] Waitress local WSGI startup and request tests passed on Windows.
- [x] pytest passes: **64 tests**, including seven deployment-specific tests.
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
- [x] Render start command verified from `wsgi:app` and installed Gunicorn source.
- [x] render.yaml uses documented fields and matches RUN.md settings.
- [x] RUN.md updated with Windows WSGI and real Render instructions.
- [x] Full suite rerun after the WSGI change.
- [x] Waitress stopped with Ctrl+C after verification; test listener released.

## Verification evidence

| Check | Result |
|---|---|
| Previous preparation baseline | 63 passed |
| Updated full pytest suite | 64 passed |
| Clean virtual environment build | `pip install -r requirements.txt` succeeded |
| WSGI regression test | Two separate processes import `wsgi:app` using one isolated new database; counts stay 24/6/8 |
| Dependency check | No broken requirements |
| Actual Waitress HTTP smoke test | 19 checks passed at `http://127.0.0.1:8000` |
| Actual Waitress browser test | 10 groups passed in headless Microsoft Edge; zero JavaScript errors |
| Responsive browser checks | Six page types at 320, 390, 768, 1024, 1440 px; no overflow |
| Fresh live WSGI database | Automatically created, then independently counted using sqlite3 |
| Clean factory import | Flask WSGI app returned, debug off, 24 films initialized |
| Git whitespace validation | `git diff --check` passed |

Fresh/repeated startup is verified in pytest temporary directories and an isolated
Waitress database under `artifacts/`. The ordinary `database/moodmovie.db` is not
deleted or replaced. Browser screenshots/report for this fix are in
`artifacts/wsgi-fix/`. Artifacts are ignored and are not part of the Git diff.
The dependency installation check from the earlier preparation remains valid;
requirements and Python 3.14.5 are unchanged by this fix.
The desktop screenshot was visually inspected. The final diff contains only the
WSGI entry file, its regression test/case audit, and deployment configuration/docs.

The Gunicorn `import_app` implementation imports the named module and retrieves
its `app` attribute. `wsgi.py` creates that attribute using the existing factory.
Its documented/source options
support `--bind`, `--workers`, and `--threads`. One worker avoids competing
first-run seed initialization; threads use existing per-operation database sessions.
Gunicorn itself was not launched natively on Windows and no Docker setup was added.

## Files changed

- `wsgi.py` (new): imports `create_app` and exposes the resulting WSGI `app`.
- `render.yaml`: points Gunicorn at `wsgi:app`, retaining existing server options.
- `tests/test_deployment.py`: adds isolated WSGI imports/restart regression coverage
  and includes `wsgi.py` in the filename-case audit.
- `RUN.md`, `DEPLOY_CHECKLIST.md`: exact commands, settings, evidence, and limitations.

The Flask factory, models, routes, services, repositories, database logic, and
UI were preserved. Only the minimal production entry file was added; no secrets,
account system, or ORM replacement was introduced. Original specifications are untouched;
the overview is still named `READEAM.md` as supplied.

## Hosted verification still to perform

- [ ] Commit and push these changes to the GitHub `main` branch.
- [ ] Update the existing Render service's Start Command to the documented
  `wsgi:app` command, save, and redeploy the latest commit (or sync its blueprint).
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
