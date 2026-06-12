# === Stage 14: Add file load support with fallback demo data ===
# Project: CraftFlow
def load_data(path=None):
    if path and os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            pass
    return {
        "materials": [{"name": "Wood", "cost": 10.5}, {"name": "Glue", "cost": 2.0}],
        "milestones": [{"title": "Design", "date": "2023-01-01"}],
        "inspiration": ["Nature patterns", "Minimalist design"]
    }
