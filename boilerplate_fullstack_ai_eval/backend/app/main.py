"""FastAPI application for the AI Evaluation Platform.

Provides REST endpoints for managing evaluation runs, a WebSocket
endpoint for live evaluation progress, and CORS configuration for
the Angular frontend.
"""

from __future__ import annotations

import asyncio
import json
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from .models.evaluation import EvaluationRunDB, init_db
from .routers import evaluations


# Active WebSocket connections keyed by evaluation run ID
active_connections: dict[str, list[WebSocket]] = {}


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Initialize database on startup."""
    await init_db()
    yield


app = FastAPI(
    title="AI Evaluation Platform",
    description="Self-hosted evaluation monitoring for LLM-powered products",
    version="0.1.0",
    lifespan=lifespan,
)

# CORS for Angular frontend (default dev port 4200)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(evaluations.router, prefix="/api/evaluations", tags=["evaluations"])


@app.get("/api/health")
async def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy", "version": "0.1.0"}


@app.websocket("/ws/evaluations/{run_id}")
async def evaluation_progress(websocket: WebSocket, run_id: str) -> None:
    """WebSocket endpoint for live evaluation progress.

    Clients connect to receive real-time updates as evaluators complete.
    Messages are JSON objects with the structure:
        {
            "type": "progress" | "result" | "complete" | "error",
            "data": { ... }
        }
    """
    await websocket.accept()

    if run_id not in active_connections:
        active_connections[run_id] = []
    active_connections[run_id].append(websocket)

    try:
        # Keep connection alive and listen for client messages
        while True:
            data = await websocket.receive_text()
            # Client can send "ping" to keep alive
            if data == "ping":
                await websocket.send_text(json.dumps({"type": "pong"}))
    except WebSocketDisconnect:
        active_connections[run_id].remove(websocket)
        if not active_connections[run_id]:
            del active_connections[run_id]


async def broadcast_to_run(run_id: str, message: dict) -> None:
    """Send a message to all WebSocket clients watching a specific run.

    Args:
        run_id: The evaluation run ID.
        message: The message dict to serialize and send.
    """
    connections = active_connections.get(run_id, [])
    payload = json.dumps(message, default=str)
    disconnected: list[WebSocket] = []

    for ws in connections:
        try:
            await ws.send_text(payload)
        except Exception:
            disconnected.append(ws)

    for ws in disconnected:
        connections.remove(ws)
