# 🇩🇪 Germany Trip Planner (MVP)

> **AI-based, student-friendly travel planner focused on trips inside Germany.**  
> Plan activities, estimate budgets, and get free drinking water tips – powered by **FastAPI + Gemini + React + Tailwind**.

---

<p align="center">
  <img src="docs/hero-mock.png" alt="Germany Trip Planner mockup" width="600" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/backend-FastAPI-009688?logo=fastapi" />
  <img src="https://img.shields.io/badge/frontend-React-61DAFB?logo=react&logoColor=black" />
  <img src="https://img.shields.io/badge/AI-Gemini-4285F4?logo=google" />
  <img src="https://img.shields.io/badge/style-Tailwind%20CSS-38BDF8?logo=tailwindcss" />
</p>

---

## ✨ What this project does

This is an **MVP for an AI co-pilot for travelling in Germany**:

- 🧭 **City trip planning**  
  Ask for a trip to a German city (e.g. Berlin, Munich) with dates, budget, and interests.
- 📅 **Day-by-day itinerary**  
  The backend uses **Gemini** to create a structured, human-readable itinerary in markdown.
- 💶 **Budget awareness**  
  You send a budget in EUR; the AI suggests low-cost / student-friendly activities.
- 🚰 **Free drinking water tips**  
  Curated POI data includes hints on **where to refill water bottles** around big sights.
- 🧱 **Modular architecture**  
  Clean separation of:
  - `FastAPI` backend  
  - `POIRepository` (data)  
  - `PlannerService` (domain logic)  
  - `LLMClient` (Gemini)  
  - `React + Tailwind` frontend

All logic is scoped to **Germany**, making it easier to later plug in real data sources (OpenStreetMap, DB APIs, hostel providers, etc.).

---

## 🧱 Tech Stack

**Backend**

- Python 3.x
- FastAPI
- Pydantic
- `google-genai` (Gemini API client)
- Uvicorn

**Frontend**

- React + TypeScript
- Vite
- Tailwind CSS
- `react-markdown` for rendering AI itineraries

---

## 📐 Architecture (high-level)

```mermaid
flowchart LR
  U("User")
  FE("Frontend (React + Vite)")
  API("Backend (FastAPI)")
  PS("PlannerService")
  PR("POIRepository")
  LC("LLMClient (Gemini)")

  U --> FE
  FE --> API
  API --> PS
  PS --> PR
  PS --> LC
  LC --> PS
  PS --> FE
  FE --> U

  PS --> PR[POIRepository]
  PS --> LC[LLMClient - Gemini]
  LC --> PS
  PS --> FE
  FE --> U
 **```**
