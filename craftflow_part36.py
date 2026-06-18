# === Stage 36: Add templates for quickly creating common records ===
# Project: CraftFlow
from datetime import date, timedelta
import random

def create_material(name: str, qty: float, cost: float) -> dict:
    return {"name": name, "qty": qty, "cost": cost, "date": date.today().isoformat()}

def add_milestone(title: str, target_date: str = None) -> dict:
    if not target_date:
        target_date = (date.today() + timedelta(days=random.randint(14, 60))).isoformat()
    return {"title": title, "status": "pending", "target_date": target_date}

def log_inspiration(source: str, note: str) -> dict:
    return {"source": source, "note": note, "date": date.today().isoformat()}
