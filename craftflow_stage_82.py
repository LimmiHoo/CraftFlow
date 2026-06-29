# === Stage 82: Add an end-to-end demo function that prints a complete walkthrough ===
# Project: CraftFlow
def run_demo():
    from datetime import date
    project = {
        "name": "Wooden Birdhouse",
        "materials": ["Pine wood: 2 boards", "Nails: 50 pcs"],
        "milestones": [{"done": True, "date": date(2024,1,1), "desc": "Cut lumber"}, {"done": False, "date": None, "desc": "Assemble frame"}],
        "costs": {"wood": 15.0, "nails": 2.5},
        "inspiration": "Minimalist design from Pinterest"
    }
    print(f"Project: {project['name']}")
    for mat in project["materials"]: print(f" - {mat}")
    total_cost = sum(project["costs"].values())
    print(f"Total Cost: ${total_cost:.2f}")
    for m in project["milestones"]: status = "✓" if m["done"] else "○"; print(f"[{status}] {m['desc']}")
    print(f"Inspiration: {project['inspiration']}")
