from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.api.v1 import trip
import os

app = FastAPI(title="AI Trip Planner API")

# Define the path to the frontend directory
FRONTEND_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "frontend")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the API router
app.include_router(trip.router, prefix="/api/v1")

# Mount the static files (CSS, JS)
app.mount("/static", StaticFiles(directory=os.path.join(FRONTEND_DIR)), name="static")

@app.get("/")
async def read_index():
    """Serves the index.html file."""
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint."""
    return {"status": "ok"}
