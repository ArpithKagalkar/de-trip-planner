from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field


class TravelPlanRequest(BaseModel):
    city: str = Field(..., description="German city name, e.g. 'Berlin'")
    start_date: date
    end_date: date
    budget_eur: float = Field(..., ge=0, description="Total budget in EUR")
    interests: List[str] = Field(
        default_factory=list,
        description="High level interests like ['museums', 'nightlife', 'nature']",
    )


class TravelPlanResponse(BaseModel):
    city: str
    start_date: date
    end_date: date
    budget_eur: float
    currency: str = "EUR"
    itinerary: str = Field(
        ..., description="Markdown formatted itinerary + budget breakdown"
    )


class POI(BaseModel):
    """
    Minimal in-memory POI model.
    Later you can back this with a real DB or external APIs.
    """

    id: str
    city: str
    name: str
    category: str
    description: str
    min_cost_eur: float
    typical_cost_eur: float
    indoor: bool
    recommended_time_of_day: str
    recommended_seasons: List[str]
    free_drinking_water_tip: Optional[str] = None
