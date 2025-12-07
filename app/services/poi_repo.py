from typing import List
from app.models.schemas import POI


class POIRepository:
    """
    Simple in-memory repository.
    Replace later with a database or external APIs.
    """

    def __init__(self) -> None:
        self._pois: List[POI] = self._seed_pois()

    def _seed_pois(self) -> List[POI]:
        # For now: a few Berlin examples as a starting point
        return [
            POI(
                id="berlin-brandenburg-gate",
                city="Berlin",
                name="Brandenburger Tor",
                category="landmark",
                description="Iconic city gate at Pariser Platz, close to Reichstag and Tiergarten.",
                min_cost_eur=0.0,
                typical_cost_eur=0.0,
                indoor=False,
                recommended_time_of_day="evening",
                recommended_seasons=["spring", "summer", "autumn", "winter"],
                free_drinking_water_tip=(
                    "Look for public drinking fountains around Pariser Platz and Tiergarten "
                    "(Berlin has many public water fountains, often marked 'Trinkwasser')."
                ),
            ),
            POI(
                id="berlin-museum-island",
                city="Berlin",
                name="Museum Island",
                category="museum",
                description="Cluster of world-class museums on an island in the Spree.",
                min_cost_eur=0.0,  # some free outdoor views / combo tickets available
                typical_cost_eur=12.0,
                indoor=True,
                recommended_time_of_day="morning",
                recommended_seasons=["autumn", "winter", "spring", "summer"],
                free_drinking_water_tip=(
                    "Inside larger museums you can usually refill bottles in restrooms; "
                    "also check nearby public fountains in Mitte."
                ),
            ),
            POI(
                id="berlin-tempelhofer-feld",
                city="Berlin",
                name="Tempelhofer Feld",
                category="park",
                description="Former airport turned huge park for skating, biking and BBQ.",
                min_cost_eur=0.0,
                typical_cost_eur=0.0,
                indoor=False,
                recommended_time_of_day="afternoon",
                recommended_seasons=["spring", "summer", "autumn"],
                free_drinking_water_tip=(
                    "In warm seasons some water fountains and park toilets have taps you can use."
                ),
            ),
        ]

    def get_pois_for_city(self, city: str) -> List[POI]:
        city_norm = city.strip().lower()
        return [poi for poi in self._pois if poi.city.lower() == city_norm]
