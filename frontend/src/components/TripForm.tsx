import { useState } from "react";
import type { FormEvent } from "react";
import type { TravelPlanRequest } from "../types";



interface TripFormProps {
  onSubmit: (payload: TravelPlanRequest) => void;
  loading: boolean;
  cities: string[]; // new
}

export function TripForm({ onSubmit, loading, cities }: TripFormProps) {
  const defaultCity = cities[0] ?? "Berlin";
  const [city, setCity] = useState(defaultCity);
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [budget, setBudget] = useState(250);
  const [interests, setInterests] = useState("museums, nightlife, parks");

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    if (!startDate || !endDate) return;

    const payload: TravelPlanRequest = {
      city,
      start_date: startDate,
      end_date: endDate,
      budget_eur: budget,
      interests: interests
        .split(",")
        .map((s) => s.trim())
        .filter(Boolean),
    };

    onSubmit(payload);
  };

  const cityOptions = cities.length > 0 ? cities : ["Berlin"];

  return (
    <form
      onSubmit={handleSubmit}
      className="rounded-2xl border border-slate-800 bg-slate-900/70 backdrop-blur-md px-4 py-5 shadow-soft space-y-5"
    >
      <div className="flex items-center justify-between gap-3">
        <div>
          <h2 className="text-lg font-semibold tracking-tight">
            Plan your next trip 🧳
          </h2>
          <p className="text-xs text-slate-400 mt-0.5">
            Focused on German cities and student budgets.
          </p>
        </div>
      </div>

      <div className="grid gap-4 sm:grid-cols-2">
        <label className="flex flex-col gap-1 text-sm">
          <span className="text-slate-300">City (Germany)</span>
          <select
            className="rounded-xl border border-slate-700 bg-slate-950/60 px-3 py-2 text-sm text-slate-50 outline-none focus:border-emerald-400 focus:ring-1 focus:ring-emerald-500/60"
            value={city}
            onChange={(e) => setCity(e.target.value)}
          >
            {cityOptions.map((c) => (
              <option key={c} value={c}>
                {c}
              </option>
            ))}
          </select>
          <span className="text-[11px] text-slate-500 mt-0.5">
            Currently seeded with curated POIs for a few major cities.
          </span>
        </label>

        <label className="flex flex-col gap-1 text-sm">
          <span className="text-slate-300">Budget (€)</span>
          <input
            type="number"
            className="rounded-xl border border-slate-700 bg-slate-950/60 px-3 py-2 text-sm text-slate-50 outline-none focus:border-emerald-400 focus:ring-1 focus:ring-emerald-500/60"
            value={budget}
            onChange={(e) => setBudget(Number(e.target.value))}
            min={0}
          />
        </label>

        <label className="flex flex-col gap-1 text-sm">
          <span className="text-slate-300">Start date</span>
          <input
            type="date"
            className="rounded-xl border border-slate-700 bg-slate-950/60 px-3 py-2 text-sm text-slate-50 outline-none focus:border-emerald-400 focus:ring-1 focus:ring-emerald-500/60"
            value={startDate}
            onChange={(e) => setStartDate(e.target.value)}
          />
        </label>

        <label className="flex flex-col gap-1 text-sm">
          <span className="text-slate-300">End date</span>
          <input
            type="date"
            className="rounded-xl border border-slate-700 bg-slate-950/60 px-3 py-2 text-sm text-slate-50 outline-none focus:border-emerald-400 focus:ring-1 focus:ring-emerald-500/60"
            value={endDate}
            onChange={(e) => setEndDate(e.target.value)}
          />
        </label>
      </div>

      <label className="flex flex-col gap-1 text-sm">
        <span className="text-slate-300">Interests (comma-separated)</span>
        <input
          className="rounded-xl border border-slate-700 bg-slate-950/60 px-3 py-2 text-sm text-slate-50 outline-none focus:border-emerald-400 focus:ring-1 focus:ring-emerald-500/60"
          value={interests}
          onChange={(e) => setInterests(e.target.value)}
          placeholder="museums, nightlife, nature..."
        />
        <span className="text-[11px] text-slate-500 mt-0.5">
          Example: <code>history, cheap food, viewpoints</code>
        </span>
      </label>

      <button
        type="submit"
        disabled={loading}
        className="inline-flex items-center justify-center rounded-xl bg-emerald-500 px-4 py-2.5 text-sm font-semibold text-slate-950 shadow-sm hover:bg-emerald-400 disabled:cursor-not-allowed disabled:opacity-60 transition-colors"
      >
        {loading ? "Planning your trip..." : "Generate itinerary"}
      </button>
    </form>
  );
}
