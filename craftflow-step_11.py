# === Stage 11: Add JSON export for the current application state ===
# Project: CraftFlow
def export_state_to_json():
    import json
    from pathlib import Path
    
    data = {
        "materials": list(CRAFT_FLOW.materials.values()),
        "milestones": list(CRAFT_FLOW.milestones.values()),
        "costs": dict(CRAFT_FLOW.costs),
        "inspiration_notes": list(CRAFT_FLOW.inspiration_notes.values())
    }
    
    output_path = Path("craftflow_state.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"State exported to {output_path}")
