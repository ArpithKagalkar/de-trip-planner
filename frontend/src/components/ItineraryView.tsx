
import ReactMarkdown from "react-markdown";
import type { TravelPlanResponse } from "../types";

interface ItineraryViewProps {
  data: TravelPlanResponse | null;
  loading: boolean;
}

export function ItineraryView({ data, loading }: ItineraryViewProps) {
  if (!data && !loading) {
    return (
      <div className="rounded-2xl border border-dashed border-slate-700/80 bg-slate-900/40 px-4 py-6 text-sm text-slate-400">
        No itinerary yet. Fill the form on the left and click{" "}
        <span className="font-medium text-slate-200">&quot;Generate itinerary&quot;</span>.
      </div>
    );
  }

  return (
    <div className="rounded-2xl border border-slate-800 bg-slate-900/70 backdrop-blur-md px-4 py-4 shadow-soft">
      {loading && (
        <div className="mb-3 text-xs text-slate-400 flex items-center gap-2">
          <span className="h-2 w-2 rounded-full bg-emerald-400 animate-pulse" />
          Generating itinerary…
        </div>
      )}

      {data && (
        <>
          <div className="mb-3 text-xs text-slate-400 flex flex-wrap items-center gap-2">
            <span className="rounded-full bg-slate-900/80 px-2 py-1 border border-slate-700/80">
              {data.city}
            </span>
            <span>
              {data.start_date} → {data.end_date}
            </span>
            <span className="text-slate-500">
              Budget:&nbsp;
              <span className="text-slate-100 font-medium">
                {data.budget_eur} {data.currency}
              </span>
            </span>
          </div>

          <div className="markdown-scroll max-h-[70vh] overflow-y-auto pr-2">
            <div className="markdown-body">
              <ReactMarkdown>{data.itinerary}</ReactMarkdown>
            </div>
          </div>
        </>
      )}
    </div>
  );
}
