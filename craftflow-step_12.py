# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: CraftFlow
import json
from pathlib import Path

def load_safe(filepath: str) -> list[dict]:
    path = Path(filepath)
    if not path.exists():
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return [item for item in data if isinstance(item, dict)]
            return []
    except (json.JSONDecodeError, IOError) as e:
        print(f"Warning: Could not parse {filepath}: {e}")
        return []

def save_safe(filepath: str, items: list[dict]) -> bool:
    path = Path(filepath)
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(items, f, indent=2, ensure_ascii=False)
        return True
    except IOError as e:
        print(f"Error writing to {filepath}: {e}")
        return False
