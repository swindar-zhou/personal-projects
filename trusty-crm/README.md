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
