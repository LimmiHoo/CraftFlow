# === Stage 46: Add a schema version field and migration helper ===
# Project: CraftFlow
from pathlib import Path
import json, uuid
VERSION = "1.1"
SCHEMA_VERSION_KEY = "__schema_version__"

def migrate_project(project_path: Path) -> None:
    if project_path.exists():
        data = load_json(project_path)
        current_ver = data.get(SCHEMA_VERSION_KEY, 0)
        if current_ver < VERSION:
            print(f"Migrating {project_path} from v{current_ver} to v{VERSION}")
            data[SCHEMA_VERSION_KEY] = VERSION
            save_json(project_path, data)

def load_json(path: Path) -> dict:
    try: return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError: return {}

def save_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
