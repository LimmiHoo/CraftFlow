# === Stage 13: Add file save support using a configurable path ===
# Project: CraftFlow
import os, json, pathlib
from datetime import datetime
class Config:
    def __init__(self):
        self.data_dir = Path(os.getenv("CRAFTFLOW_DATA", "data"))
        self.project_file = self.data_dir / "projects.json"
        self.init_dirs()
    def init_dirs(self):
        self.data_dir.mkdir(parents=True, exist_ok=True)
    def save_project(self, project_data):
        with open(self.project_file, 'w', encoding='utf-8') as f:
            json.dump(project_data, f, indent=2, ensure_ascii=False)
        return True
