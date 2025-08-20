# Trusty CRM — Frontend (Next.js)

## Setup
- Node 20+
- pnpm

## Install & Run
```bash
pnpm install
pnpm dev
```

## Env
Create `.env.local` (see keys below):
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Tech
- Next.js 14 (App Router, TS)
- Tailwind CSS
- TanStack Query

## Structure
- `src/app/*`: routes and layout
- `src/components/*`: shared UI
- `src/lib/*`: API client, providers, types
- `src/styles/*`: global css 