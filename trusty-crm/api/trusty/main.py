from fastapi import FastAPI
from loguru import logger

app = FastAPI(title="Trusty CRM API")

@app.get("/healthz")
def health():
    return {"ok": True}
