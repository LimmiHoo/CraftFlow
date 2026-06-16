# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: CraftFlow
from datetime import datetime, timedelta
def get_upcoming_items(items: list[dict], days_ahead: int = 7) -> list[dict]:
    now = datetime.now()
    cutoff = now + timedelta(days=days_ahead)
    return [item for item in items if item.get('due_date') and now <= datetime.fromisoformat(item['due_date']) < cutoff]

def get_overdue_items(items: list[dict]) -> list[dict]:
    now = datetime.now()
    return [item for item in items if item.get('due_date') and datetime.fromisoformat(item['due_date']) < now]
