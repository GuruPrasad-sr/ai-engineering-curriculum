# Full-Stack AI Evaluation Platform

A self-hosted evaluation monitoring platform for AI teams. This is not a generic CRUD app — it is the kind of internal tool that teams building LLM-powered products actually need.

## What This Platform Does

- **Run evaluations** against your AI systems from a web dashboard or API
- **Compare results** across model versions, prompt changes, or configuration updates
- **Track trends** over time — catch regressions before they reach production
- **Audit trails** — every evaluation run is recorded with full context
- **Live progress** — watch evaluations run in real-time via WebSocket

## Architecture

```
┌─────────────────────────────────┐
│        Angular Frontend          │
│  ┌──────────┬──────┬──────────┐ │
│  │Dashboard │Compare│ Detail  │ │
│  │Component │ View  │ View    │ │
│  └────┬─────┴──┬───┴────┬────┘ │
│       │  NgRx Store      │      │
│       │  (state mgmt)    │      │
└───────┼──────────────────┼──────┘
        │  HTTP + WebSocket │
┌───────┼──────────────────┼──────┐
│       │  FastAPI Backend  │      │
│  ┌────▼─────┬──────┬─────▼───┐  │
│  │ Eval API │Router│ WS Live │  │
│  └────┬─────┴──┬───┴────┬───┘  │
│  ┌────▼─────┐  │  ┌─────▼───┐  │
│  │EvalRunner│  │  │ SQLite/ │  │
│  │ Service  │  │  │Postgres │  │
│  └──────────┘  │  └─────────┘  │
└────────────────┼────────────────┘
                 │
         ┌───────▼───────┐
         │  LLM APIs     │
         │  (OpenAI, etc)│
         └───────────────┘
```

## Quick Start

### Backend

```bash
cd backend
python -m venv .venv
.venv/Scripts/activate    # Windows
# source .venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

API docs available at `http://localhost:8000/docs`

### Frontend

See `frontend/ANGULAR_SETUP.md` for full Angular setup instructions.

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/evaluations/run` | Start a new evaluation run |
| `GET` | `/api/evaluations/` | List all evaluation runs |
| `GET` | `/api/evaluations/{id}` | Get evaluation run details |
| `GET` | `/api/evaluations/{id}/results` | Get results for a run |
| `POST` | `/api/evaluations/compare` | Compare two evaluation runs |
| `DELETE` | `/api/evaluations/{id}` | Delete an evaluation run |
| `WS` | `/ws/evaluations/{id}` | Live evaluation progress |

## Project Structure

```
backend/
├── app/
│   ├── main.py              # FastAPI application + WebSocket
│   ├── models/
│   │   └── evaluation.py    # Pydantic/SQLModel data models
│   ├── routers/
│   │   └── evaluations.py   # API route handlers
│   └── services/
│       └── eval_runner.py    # Evaluation orchestration service
└── requirements.txt

frontend/
└── ANGULAR_SETUP.md          # Angular component architecture + setup
```

## Design Principles

1. **Evaluation-first**: Every feature exists to make running and understanding evaluations easier
2. **Async throughout**: Evaluations are I/O-bound; the entire backend is async
3. **Compare everything**: Every result is stored for comparison against future runs
4. **Self-contained**: Runs locally with SQLite; optionally upgrade to Postgres for teams
