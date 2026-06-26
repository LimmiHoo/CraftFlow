# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: CraftFlow
def reset_demo_data():
    import json, os
    from pathlib import Path
    
    base = Path(__file__).parent
    data_file = base / "demo_data.json"
    
    demo_records = {
        "materials": [
            {"id": 101, "name": "Clay", "cost": 5.99, "stock": 2},
            {"id": 102, "name": "Glaze", "cost": 3.49, "stock": 5}
        ],
        "milestones": [
            {"id": 201, "title": "Design Sketch", "status": "pending"},
            {"id": 202, "title": "Prototype Build", "status": "in_progress"}
        ],
        "costs": [
            {"id": 301, "project_id": 5, "amount": 12.50, "date": "2024-01-15"},
            {"id": 302, "project_id": 6, "amount": 8.75, "date": "2024-01-16"}
        ],
        "inspiration": [
            {"id": 401, "source": "Nature", "note": "River curves inspire flow lines"},
            {"id": 402, "source": "Architecture", "note": "Minimalist bridges for structure ideas"}
        ]
    }
    
    try:
        with open(data_file, 'w', encoding='utf-8') as f:
            json.dump(demo_records, f, indent=2)
        print(f"[OK] Demo data reset successfully written to {data_file}")
    except Exception as e:
        print(f"[ERROR] Failed to reset demo data: {e}")
