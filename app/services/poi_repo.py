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
        return [
            # --- BERLIN ---
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
                min_cost_eur=0.0,
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

            # --- MUNICH ---
            POI(
                id="munich-marienplatz",
                city="Munich",
                name="Marienplatz & Old Town",
                category="landmark",
                description="Central square with the New Town Hall and Glockenspiel.",
                min_cost_eur=0.0,
                typical_cost_eur=0.0,
                indoor=False,
                recommended_time_of_day="morning",
                recommended_seasons=["spring", "summer", "autumn", "winter"],
                free_drinking_water_tip=(
                    "Look for public fountains near churches; you can also refill in café restrooms "
                    "if you buy a cheap drink."
                ),
            ),
            POI(
                id="munich-englischer-garten",
                city="Munich",
                name="Englischer Garten",
                category="park",
                description="Huge city park with rivers, beer gardens and the Eisbach surfers.",
                min_cost_eur=0.0,
                typical_cost_eur=0.0,
                indoor=False,
                recommended_time_of_day="afternoon",
                recommended_seasons=["spring", "summer", "autumn"],
                free_drinking_water_tip=(
                    "Near beer gardens and kiosks you can usually find restrooms for refilling "
                    "your bottle; some public fountains in summer."
                ),
            ),
            POI(
                id="munich-deutsches-museum",
                city="Munich",
                name="Deutsches Museum",
                category="museum",
                description="Huge science & technology museum, ideal for bad weather days.",
                min_cost_eur=8.0,
                typical_cost_eur=15.0,
                indoor=True,
                recommended_time_of_day="morning",
                recommended_seasons=["winter", "autumn", "spring", "summer"],
                free_drinking_water_tip=(
                    "Inside the museum you can use restrooms to refill water; "
                    "there are supermarkets along the Isar."
                ),
            ),

            # --- HAMBURG ---
            POI(
                id="hamburg-hafen-city",
                city="Hamburg",
                name="HafenCity & Elbphilharmonie",
                category="landmark",
                description="Modern harbour district with great views and iconic concert hall.",
                min_cost_eur=0.0,
                typical_cost_eur=0.0,
                indoor=False,
                recommended_time_of_day="afternoon",
                recommended_seasons=["spring", "summer", "autumn"],
                free_drinking_water_tip=(
                    "Public fountains and restrooms around Landungsbrücken and HafenCity; "
                    "many cafes will refill bottles if you order something small."
                ),
            ),
            POI(
                id="hamburg-miniatur-wunderland",
                city="Hamburg",
                name="Miniatur Wunderland",
                category="museum",
                description="World’s largest model railway exhibition, super detailed and popular.",
                min_cost_eur=10.0,
                typical_cost_eur=20.0,
                indoor=True,
                recommended_time_of_day="morning",
                recommended_seasons=["winter", "autumn", "spring", "summer"],
                free_drinking_water_tip=(
                    "Use restrooms for refilling water; supermarkets nearby in the Speicherstadt area."
                ),
            ),
            POI(
                id="hamburg-planten-un-blomen",
                city="Hamburg",
                name="Planten un Blomen",
                category="park",
                description="Beautiful park with ponds, gardens and light shows in summer.",
                min_cost_eur=0.0,
                typical_cost_eur=0.0,
                indoor=False,
                recommended_time_of_day="evening",
                recommended_seasons=["spring", "summer", "autumn"],
                free_drinking_water_tip=(
                    "Look for park fountains and public toilets; nearby U-Bahn stations "
                    "often have shops where you can buy cheap water."
                ),
            ),
        ]

    def get_pois_for_city(self, city: str) -> List[POI]:
        city_norm = city.strip().lower()
        return [poi for poi in self._pois if poi.city.lower() == city_norm]

    def list_cities(self) -> List[str]:
        """Return sorted list of unique city names we have POIs for."""
        return sorted({poi.city for poi in self._pois})
