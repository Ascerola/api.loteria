## Development quickstart

- Requirements: Docker, Docker Compose, uv (https://docs.astral.sh/uv/).
- Install deps: `uv sync`

### Run locally (app on host, DB in container)
1) Start DB: `docker compose -f docker-compose.db.yml up -d`
2) Run API: `uv run fastapi dev src/main.py`
   - Uses `DATABASE_URL` env; defaults to `postgresql://postgres:postgres@localhost:5433/postgres`.

### Run everything in containers
- `docker compose up --build`
  - App runs on http://localhost:8000 and uses the internal `db` service.

### Config
- Override via env vars: `DATABASE_URL`, `APP_HOST`, `APP_PORT`.
- Models go in `src/db/models`; schema auto-creates on first DB access.
- If port 5432 is busy on your host, the DB container publishes to `${DB_PORT:-5433}` by default. Set `DB_PORT=5432` (or another free port) when running Compose if you need a different binding. Adjust `DATABASE_URL` accordingly when connecting from the host.
