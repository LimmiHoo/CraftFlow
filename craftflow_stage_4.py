# === Stage 4: Implement create operations for the primary records ===
# Project: CraftFlow
from datetime import datetime
import json
import os

def create_record(record_type, data):
    """
    Creates a new record (Material, Milestone, Cost, or Inspiration) and saves it to the project file.
    Expects 'data' dict with 'name', 'description', and optional fields like 'date', 'amount', 'link'.
    """
    if not os.path.exists("craftflow_data.json"):
        open("craftflow_data.json", "w").close()
    
    with open("craftflow_data.json", "r") as f:
        records = json.load(f)
    
    record_id = len(records) + 1
    new_record = {
        "id": record_id,
        "type": record_type,
        "name": data.get("name"),
        "description": data.get("description", ""),
        "date": datetime.now().strftime("%Y-%m-%d") if data.get("date") is None else data["date"],
        **{k: v for k, v in data.items() if k not in ["name", "description", "date"]}
    }
    
    records.append(new_record)
    
    with open("craftflow_data.json", "w") as f:
        json.dump(records, f, indent=2)
    
    return new_record

# Example usage:
# create_record("Material", {"name": "Canvas", "description": "Heavy texture white canvas", "cost": 45.0})
