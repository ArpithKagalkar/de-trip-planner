import { useEffect, useState } from "react";
import { TripForm } from "./components/TripForm";
import { ItineraryView } from "./components/ItineraryView";
import type { TravelPlanRequest, TravelPlanResponse } from "./types";

const API_BASE = "http://127.0.0.1:8000";

function App() {
  const [loading, setLoading] = useState(false);
  const [itinerary, setItinerary] = useState<TravelPlanResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [cities, setCities] = useState<string[]>([]);

  useEffect(() => {
    // Load supported cities from backend
    const loadCities = async () => {
      try {
        const res = await fetch(`${API_BASE}/cities`);
        if (!res.ok) return; // silent fail, fallback to defaults
        const data: string[] = await res.json();
        setCities(data);
      } catch (err) {
        console.error("Failed to load cities", err);
      }
    };

    loadCities();
  }, []);

  const handleSubmit = async (payload: TravelPlanRequest) => {
    setLoading(true);
    setError(null);

    try {
      const res = await fetch(`${API_BASE}/plan`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      if (!res.ok) {
        const body = await res.json().catch(() => ({}));
        throw new Error(body.detail || `Request failed with ${res.status}`);
      }

      const data: TravelPlanResponse = await res.json();
      setItinerary(data);
    } catch (err: any) {
      console.error(err);
      setError(err.message || "Something went wrong");
      setItinerary(null);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950 text-slate-50">
      <div className="max-w-6xl mx-auto px-4 py-8">
        {/* Header */}
        <header className="mb-8 flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
          <div>
            <h1 className="text-3xl sm:text-4xl font-semibold tracking-tight">
              🇩🇪 Germany Trip Planner
            </h1>
            <p className="text-sm text-slate-400 mt-1 max-w-xl">
              Plan student-friendly trips inside Germany: activities, budget
              estimate and free drinking-water tips in one place.
            </p>
          </div>

          <div className="flex items-center gap-2 text-xs sm:text-sm text-slate-300">
            <span className="inline-flex items-center gap-1 rounded-full bg-slate-900/80 px-3 py-1 border border-slate-700/80">
              <span className="h-2 w-2 rounded-full bg-emerald-400 animate-pulse" />
              Live · Gemini-powered
            </span>
          </div>
        </header>

        {/* Main content: 2 columns */}
        <div className="grid gap-6 lg:grid-cols-[minmax(0,1.1fr)_minmax(0,1.7fr)] items-start">
          <TripForm onSubmit={handleSubmit} loading={loading} cities={cities} />

          <div className="space-y-3">
            {error && (
              <div className="rounded-2xl border border-red-900/70 bg-red-950/50 px-4 py-3 text-sm text-red-100 shadow-soft">
                {error}
              </div>
            )}
            <ItineraryView data={itinerary} loading={loading} />
          </div>
        </div>

        <footer className="mt-8 text-[11px] text-slate-500 flex justify-between flex-wrap gap-2">
          <span>v0.1 · local prototype</span>
          <span>Backend: FastAPI · Frontend: React + Vite + Tailwind</span>
        </footer>
      </div>
    </div>
  );
}

export default App;
