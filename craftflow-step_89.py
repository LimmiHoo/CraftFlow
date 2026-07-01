# === Stage 89: Add final consistency checks for names, statuses, and dates ===
# Project: CraftFlow
def validate_consistency(db):
    for entry in db:
        if not entry['name'].strip(): raise ValueError("Name cannot be empty")
        if entry['status'] not in ['planned', 'in_progress', 'completed']: raise ValueError(f"Invalid status: {entry['status']}")
        try:
            datetime.fromisoformat(entry['date'])
        except (ValueError, TypeError): raise ValueError("Date must be ISO format string")
    return True
