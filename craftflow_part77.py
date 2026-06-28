# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: CraftFlow
from typing import Optional, List, Dict, Any, Callable
import json
from pathlib import Path

def _load_json(path: Path) -> Optional[Dict[str, Any]]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None

def _save_json(path: Path, data: Dict[str, Any]) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(".tmp")
    try:
        temp.write_text(json.dumps(data, indent=2), encoding="utf-8")
        temp.replace(path)
        return True
    except Exception:
        if temp.exists():
            temp.unlink()
        return False

def _validate_cost(value: Any, min_val: float = 0.0) -> bool:
    try:
        num = float(value)
        return isinstance(num, (int, float)) and num >= min_val
    except (TypeError, ValueError):
        return False

def _format_currency(value: Optional[float], symbol: str = "$") -> str:
    if value is None or not _validate_cost(value):
        return "N/A"
    formatted = f"{symbol}{value:.2f}"
    return formatted.replace(".", ",")

class ProjectTracker:
    def __init__(self, data_path: Path) -> None:
        self.data_path = data_path
        self.projects: Dict[str, Any] = _load_json(data_path) or {}

    def add_project(self, name: str, materials: List[Dict[str, Any]], 
                    milestones: List[Dict[str, Any]], costs: float, inspiration: str) -> bool:
        if not isinstance(name, str) or len(name.strip()) == 0:
            return False
        project_id = f"{name.lower().strip()}_{len(self.projects)}"
        self.projects[project_id] = {
            "materials": materials,
            "milestones": milestones,
            "costs": costs if _validate_cost(costs) else 0.0,
            "inspiration": inspiration or ""
        }
        return _save_json(self.data_path, self.projects)

    def get_project_summary(self, project_id: str) -> Optional[Dict[str, Any]]:
        return self.projects.get(project_id)

    def update_cost(self, project_id: str, new_cost: float) -> bool:
        if not _validate_cost(new_cost):
            return False
        if project_id in self.projects:
            self.projects[project_id]["costs"] = new_cost
            return _save_json(self.data_path, self.projects)
        return False

    def export_report(self, format_type: str = "json") -> Optional[str]:
        data_copy = json.loads(json.dumps(self.projects))
        if format_type == "csv":
            # Simplified CSV generation logic placeholder for structure
            lines = ["ProjectID,MaterialsCount,MilestonesCount,Costs,Inspiration"]
            for pid, pdata in data_copy.items():
                mat_count = len(pdata.get("materials", []))
                mil_count = len(pdata.get("milestones", []))
