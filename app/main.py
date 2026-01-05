from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # ✅ new


from app.config import ensure_config
from app.models.schemas import TravelPlanRequest, TravelPlanResponse
from app.services.poi_repo import POIRepository
from app.services.ll_client import LLMClient
from app.services.planner_service import PlannerService

ensure_config()

app = FastAPI(
    title="Germany Trip Planner API",
    version="0.1.0",
    description="AI-based travel planner focused on trips within Germany.",
)

# ✅ Allow your frontend (Vite dev server) to call the API
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

_poi_repo = POIRepository()
_llm_client = LLMClient()
_planner_service = PlannerService(_poi_repo, _llm_client)


@app.get("/")
def root():
    return {
        "message": "Germany Trip Planner API is alive.",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/cities")
def list_cities() -> list[str]:
    """Return the list of cities with curated POIs."""
    return _poi_repo.list_cities()

@app.post("/plan", response_model=TravelPlanResponse)
async def create_plan(req: TravelPlanRequest):
    try:
        return _planner_service.build_plan(req)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
