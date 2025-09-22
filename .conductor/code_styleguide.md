# Code Style Guide - AI Trip Planner

## Core Principle: "Clarity Over Cleverness"

Write code that is easy to understand, maintain, and debug.

## Python Style Guidelines

### Base Style Guide
- Follow PEP 8 strictly.
- Use Black for automatic formatting (line length: 88).
- Use ruff for linting and import sorting.
- Use type hints for all function signatures.

### Naming Conventions
- **Variables**: `snake_case` (e.g., `trip_destination`).
- **Functions**: `snake_case` (e.g., `get_flight_options`).
- **Classes**: `PascalCase` (e.g., `TripRequest`).
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `FLIGHT_API_URL`).

### FastAPI-Specific Patterns

#### Pydantic Models
```python
# In app/models/trip.py
from pydantic import BaseModel, Field
from datetime import date

class TripRequest(BaseModel):
    destination: str = Field(..., description="The desired travel destination.")
    start_date: date = Field(..., description="The start date of the trip.")
    end_date: date = Field(..., description="The end date of the trip.")

class FlightOptions(BaseModel):
    airline: str
    price: float
    departure_time: str
```

#### API Endpoints
```python
# In app/api/v1/trip.py
from fastapi import APIRouter, HTTPException
from app.models.trip import TripRequest, TripDetails
from app.services.planning_service import get_trip_plan

router = APIRouter()

@router.post("/plan", response_model=TripDetails)
async def plan_trip(request: TripRequest):
    """
    Takes user's trip request and returns a comprehensive trip plan.
    """
    try:
        trip_plan = await get_trip_plan(request)
        return trip_plan
    except Exception as e:
        # In a real app, log the error
        raise HTTPException(status_code=500, detail="Failed to plan trip.")
```

### Error Handling
- Use specific exceptions where possible.
- Log errors with context.
- Return informative HTTP exceptions from API endpoints.

## Frontend Style Guidelines (HTML/JS/CSS)

### HTML
- Use semantic HTML5 tags (`<main>`, `<section>`, `<nav>`).
- Ensure all images have `alt` attributes.
- Use descriptive `id` and `class` names (e.g., `id="trip-form"`, `class="submit-button"`).

### CSS
- Use a consistent naming convention (e.g., BEM).
- Keep selectors specific but not overly nested.
- Use CSS variables for colors and fonts.

### JavaScript
- Use modern JavaScript (ES6+).
- Keep functions small and focused on a single task.
- Use `const` by default, `let` only when reassignment is needed.
- Add comments to explain complex logic.
