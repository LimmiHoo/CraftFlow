# === Stage 66: Add export of a short status dashboard ===
# Project: CraftFlow
import json, os
from datetime import datetime

def export_dashboard(data_file="craftflow_data.json"):
    try:
        with open(data_file) as f: data = json.load(f)
    except FileNotFoundError: return print("No data found.")
    
    projects = data.get("projects", [])
    total_cost = sum(p.get("costs", {}).get("total", 0) for p in projects if isinstance(p, dict))
    active_count = len([p for p in projects if "status" in p and p["status"] != "completed"])
    
    dashboard_text = f"""
=== CRAFTFLOW STATUS DASHBOARD ===
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}

[SUMMARY]
Total Projects:  {len(projects)}
Active Projects: {active_count}
Estimated Cost:  ${total_cost:.2f}

[MATERIALS & COSTS]
"""
    for p in projects[:5]:
        if isinstance(p, dict):
            name = p.get("name", "Unknown")
            costs = p.get("costs", {})
            mat_list = "\n".join(f"  - {k}: ${v}" for k, v in costs.items() if isinstance(v, (int, float)))
            dashboard_text += f"\n{name}:\n{mat_list}\n"

    dashboard_text += """
[INSPIRATION NOTES]
"""
    notes = data.get("notes", [])
    for note in notes[:3]:
        if isinstance(note, dict):
            dashboard_text += f"- {note.get('source', 'Unknown')}: {note.get('text', '')}\n"

    print(dashboard_text.strip())
