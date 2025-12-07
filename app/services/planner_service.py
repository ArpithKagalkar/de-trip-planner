from app.models.schemas import TravelPlanRequest, TravelPlanResponse
from app.services.poi_repo import POIRepository
from app.services.ll_client import LLMClient
from app.utils.time_utils import trip_length_days


class PlannerService:
    def __init__(self, poi_repo: POIRepository, llm_client: LLMClient) -> None:
        self._poi_repo = poi_repo
        self._llm_client = llm_client

    def build_plan(self, req: TravelPlanRequest) -> TravelPlanResponse:
        days = trip_length_days(req.start_date, req.end_date)
        if days <= 0:
            raise ValueError("end_date must be on or after start_date")

        pois = self._poi_repo.get_pois_for_city(req.city)
        itinerary_text = self._llm_client.generate_itinerary(req, pois)

        return TravelPlanResponse(
            city=req.city,
            start_date=req.start_date,
            end_date=req.end_date,
            budget_eur=req.budget_eur,
            itinerary=itinerary_text,
        )
