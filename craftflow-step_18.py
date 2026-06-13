# === Stage 18: Add an activity log with timestamps and action names ===
# Project: CraftFlow
import time
from datetime import datetime, timezone

class ActivityLogger:
    def __init__(self):
        self.entries = []

    def log(self, action_name: str, details: dict = None) -> None:
        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "action": action_name,
            "details": details or {}
        }
        self.entries.append(entry)

    def get_log(self) -> list:
        return sorted(self.entries, key=lambda x: x["timestamp"], reverse=True)
