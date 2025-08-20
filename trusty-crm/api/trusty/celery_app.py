from __future__ import annotations

from celery import Celery

celery_app = Celery(
    "trusty",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/1",
)

@celery_app.task
def ping() -> str:
    return "pong"
