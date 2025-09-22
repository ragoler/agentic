from fastapi import FastAPI
from app.api.v1 import trip

app = FastAPI(title="AI Trip Planner API")

app.include_router(trip.router, prefix="/api/v1")

@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint to verify the server is running.
    """
    return {"status": "ok"}
