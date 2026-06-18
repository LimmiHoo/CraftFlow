# === Stage 37: Add recommendations for the next useful action ===
# Project: CraftFlow
from datetime import datetime, timedelta
import random
from typing import List, Dict, Any

def generate_next_action(project_data: Dict[str, Any]) -> str:
    """Generates a recommended next action based on project status."""
    pending_milestones = [m for m in project_data.get("milestones", []) if not m.get("completed")]
    low_stock_items = [i for i in project_data.get("materials", []) if i.get("quantity", 10) < (i.get("required_for_next", 5))]

    suggestions = []
    
    if pending_milestones:
        next_milestone = min(pending_milestones, key=lambda x: x.get("deadline"))
        days_left = (next_milestone.get("deadline") - datetime.now()).days
        urgency = "urgent" if days_left <= 3 else "normal"
        suggestions.append(f"{urgency.capitalize()} milestone: {next_milestone['title']} ({days_left} days left)")

    if low_stock_items:
        item_name = low_stock_items[0]["name"]
        current_qty = low_stock_items[0]["quantity"]
        needed = low_stock_items[0].get("required_for_next", 5) - current_qty
        suggestions.append(f"Restock {item_name}: need at least {needed} more units")

    if not suggestions:
        inspiration_notes = project_data.get("inspiration", [])
        if inspiration_notes:
            recent_note = random.choice(inspiration_notes)
            return f"Inspiration note to explore: '{recent_note}'"
        
        return "Review completed milestones and update costs."

    return "; ".join(suggestions)
