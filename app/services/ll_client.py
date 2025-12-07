from typing import List

from google import genai

from app.config import GEMINI_API_KEY, GEMINI_MODEL
from app.models.schemas import TravelPlanRequest, POI


class LLMClient:
    """
    Thin wrapper around Gemini (via Google Gen AI SDK).
    All LLM calls go through here so you can later:
      - swap models (2.5-flash, 2.5-pro, etc.)
      - or even swap providers completely if you want.
    """

    def __init__(self, model: str | None = None) -> None:
        # Client will use the Gemini Developer API with the API key
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.model = model or GEMINI_MODEL

    def generate_itinerary(self, req: TravelPlanRequest, pois: List[POI]) -> str:
        """
        Ask Gemini for a markdown itinerary text, using our POI hints.
        """

        # Turn POIs into a compact text block
        poi_lines = []
        for poi in pois:
            seasons = ", ".join(poi.recommended_seasons)
            poi_lines.append(
                f"- {poi.name} ({poi.category}, ~{poi.typical_cost_eur:.0f} €): "
                f"{poi.description} | best time: {poi.recommended_time_of_day}, "
                f"seasons: {seasons}."
            )
            if poi.free_drinking_water_tip:
                poi_lines.append(f"  - Free water tip: {poi.free_drinking_water_tip}")

        poi_block = "\n".join(poi_lines) if poi_lines else "No curated POIs yet."

        # Trip info as JSON
        trip_json = req.model_dump_json(indent=2)

        # High-level instructions for the model
        instructions = """
You are an AI travel planner specialised in student-budget trips inside Germany.
You MUST answer in clear English and use markdown headings.
Optimise for low costs but still fun experiences.

Always think about:
- best time of day for each activity
- rough minimum budget in EUR
- where travellers can refill water bottles for free or very cheap near major sights
- keeping most things reachable by public transport or walking
"""

        # What we want back (markdown structure)
        format_instructions = """
FORMAT (markdown):

# Overview
- Short 3–5 sentence summary of the trip.

## Where to stay
- Suggest 1–2 neighbourhoods that are good & relatively cheap for hostels / budget Airbnbs.
- Give a rough *nightly* price range in EUR for a dorm bed vs a basic private room.

## Day-by-day plan
For each day:
- Morning: ...
- Afternoon: ...
- Evening: ...
Include:
- approximate cost per activity (0€ / 5–10€ / 10–20€ etc.)
- notes about weather dependence (indoor vs outdoor)

## Budget breakdown
- Minimum total budget for the whole trip (EUR)
- Breakdown: accommodation, food, transport, activities, buffer

## Free drinking water
- Bullet list of where to find free or very cheap drinking water near the main sights mentioned.

Important:
- Keep everything inside Germany.
- If you have no curated POIs, still use your knowledge about the city.
"""

        # Single combined prompt – Gemini text generation API
        # Example pattern based on official docs: client.models.generate_content(...).text :contentReference[oaicite:2]{index=2}
        full_prompt = f"""
{instructions}

User trip request (JSON):
{trip_json}

Curated POIs for this city:
{poi_block}

{format_instructions}
"""

        response = self.client.models.generate_content(
            model=self.model,
            contents=full_prompt,
        )

        itinerary_text: str = response.text or ""
        return itinerary_text.strip()
