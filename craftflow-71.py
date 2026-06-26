# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: CraftFlow
def get_seed_data():
    return {
        "materials": [
            {"id": 1, "name": "Canvas", "quantity": 2, "unit_cost": 25.0},
            {"id": 2, "name": "Acrylic Paint Set", "quantity": 1, "unit_cost": 45.0},
        ],
        "milestones": [
            {"id": 1, "title": "Sketch Approval", "due_date": "2023-11-01"},
            {"id": 2, "title": "Base Layer Complete", "due_date": "2023-11-15"},
        ],
        "costs": [
            {"category": "Materials", "amount": 95.0},
            {"category": "Software License", "amount": 0.0},
        ],
        "inspiration_notes": [
            {"source": "National Gallery", "url": "https://www.nationalgallery.org.uk/", "tags": ["classics"]},
            {"source": "Behance", "url": "https://www.behance.net/", "tags": ["modern"]}
        ]
    }
