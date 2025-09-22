from fastapi import APIRouter
from app.models.trip import TripRequest, TripPlan
from app.agents.orchestrator import OrchestratorAgent

router = APIRouter()
orchestrator = OrchestratorAgent()

@router.post("/plan", response_model=TripPlan, tags=["Planning"])
async def get_trip_plan(request: TripRequest):
    """
    Accepts a user's trip request and returns a trip plan
    coordinated by the OrchestratorAgent.
    """
    return await orchestrator.plan_trip(request)
