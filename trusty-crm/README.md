# Trusty CRM — Networking-first Job Search Assistant

**Goal:** Make networking effortless. Import your contacts & alumni lists, link them to companies you’re applying to (detected via Gmail label), and get *ranked warm intros* with one-click outreach and follow-up reminders.

## Why this exists
Most platforms optimize job applications. Real results come from **relationships**. Trusty focuses on:
- Importing your **contacts/alumni**
- Resolving them to **companies** you care about
- Suggesting **who to ping** and **when**

## Features (MVP)
- CSV contact import (LinkedIn export + alumni lists)
- Company resolution (fuzzy match employer → domain; Clearbit logos)
- Gmail label sync (read-only) → detect applications & status
- Connections view: top alumni/contacts per applied company
- Tasks & weekly digest for follow-ups

## Tech
- **Frontend:** Next.js 14 (TS), Tailwind, shadcn/ui, TanStack Query
- **Backend:** FastAPI, SQLAlchemy, Alembic, Celery+Redis
- **Data:** Postgres
- **Integrations:** Gmail API (label-scoped), optional Google People API

## Getting Started

### 1) Prereqs
- Node 20+, Python 3.11+, Docker (for Postgres/Redis), pnpm

### 2) Spin up infra
```bash
docker compose up -d

```

### 3) Run backend (API)
```bash
cd api
# activate your venv if needed
uvicorn trusty.main:app --reload --port 8000
```

### 4) Run frontend (Web)
```bash
cd app
pnpm install
# optionally set API URL (defaults to http://localhost:8000)
echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local
pnpm dev
```

## Architecture

### Frontend (app)
- Next.js 14 (App Router, TypeScript), Tailwind CSS, TanStack Query
- Structure
  - `app/src/app`: routes and layout (`/`, `/connections`, `/applications`, `/settings`, `/login`)
  - `app/src/components`: shared UI (e.g., `Navbar`)
  - `app/src/lib`: cross-cutting code (`api.ts` Axios client, `providers.tsx` for React Query, `types.ts`)
  - `app/src/styles`: global Tailwind CSS
- Config
  - `NEXT_PUBLIC_API_URL` controls API base URL (defaults to `http://localhost:8000`)

### Backend (api)
- FastAPI app with modular routers and CORS
- Entry: `trusty/main.py` (adds CORS, includes `routes.api_router`)
- Routers: `trusty/routes/{health,companies,contacts,applications,tasks}.py`
- Config: `trusty/core/config.py` (DB URL, CORS origins)
- Persistence
  - SQLAlchemy engine/session in `trusty/core/db.py`
  - Models in `trusty/models` (`Company`, `Contact`, `Application`, `Task`)
  - Pydantic schemas in `trusty/schemas`
  - Alembic: `api/alembic.ini`, `api/alembic/env.py`
- Async jobs: `trusty/celery_app.py` (Redis broker/backend)

### Infrastructure
- `docker-compose.yml`: Postgres (5432), Redis (6379), Adminer (8081)

## MVP Feature Mapping
- CSV import → UI in `app/src/app/settings`, endpoint to be added; parse CSV and create `Contact`s
- Company resolution → server-side using `rapidfuzz` to map employer → domain
- Gmail label sync → Google API client; background tasks via Celery; produces `Application` records
- Connections view → fetch `Contact`s grouped by `Company`
- Tasks & weekly digest → `Task` model + Celery periodic jobs
