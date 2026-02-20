from fastapi import FastAPI
from datetime import date

app = FastAPI(title="Football Information API")

# ---------- Static Data ----------

news_data = [
    {
        "headline": "Real Madrid win dramatic late match",
        "summary": "A last-minute goal secures all three points.",
        "date": "2026-02-18"
    },
    {
        "headline": "Champions League knockout stage begins",
        "summary": "Europe's best teams face off in high-stakes matches.",
        "date": "2026-02-17"
    }
]

matches_today = [
    {
        "home_team": "Real Madrid",
        "away_team": "Barcelona",
        "time": "21:30",
        "status": "Upcoming"
    },
    {
        "home_team": "Manchester City",
        "away_team": "Arsenal",
        "time": "23:00",
        "status": "Live"
    }
]

teams = [
    {"name": "Real Madrid", "league": "La Liga"},
    {"name": "Barcelona", "league": "La Liga"},
    {"name": "Manchester City", "league": "Premier League"},
    {"name": "Arsenal", "league": "Premier League"}
]

# ---------- API Endpoints ----------

@app.get("/news")
def get_news():
    return news_data


@app.get("/matches/today")
def get_matches_today():
    return matches_today


@app.get("/teams")
def get_teams():
    return teams
