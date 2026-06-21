# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: CraftFlow
import json
from datetime import datetime, timedelta
from pathlib import Path

def demo_craftflow():
    project = {
        "name": "Wooden Birdhouse",
        "materials": ["Pine wood", "Roofing shingles"],
        "milestones": [{"title": "Cutting", "date": "2024-10-01"}],
        "costs": 45.5,
        "inspiration": "Minimalist design"
    }

    project["materials"].append("Nails")
    project["milestones"].append({"title": "Assembly", "date": (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d")})
    project["costs"] += 5.0

    with open("craftflow_demo.json", "w", encoding="utf-8") as f:
        json.dump(project, f, indent=2)

    print(f"Demo completed for '{project['name']}'. Total cost: ${project['costs']}")
