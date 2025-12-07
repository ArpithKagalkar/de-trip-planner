export interface TravelPlanRequest {
  city: string;
  start_date: string;   // ISO date: "2025-03-01"
  end_date: string;
  budget_eur: number;
  interests: string[];
}

export interface TravelPlanResponse {
  city: string;
  start_date: string;
  end_date: string;
  budget_eur: number;
  currency: string;
  itinerary: string; // markdown
}
