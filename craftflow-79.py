# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: CraftFlow
import json, os, sys
from pathlib import Path

def validate_project():
    errors = []
    if not (project_dir := Path(__file__).parent): return errors
    for f in ['materials.json', 'milestones.json', 'costs.json', 'inspiration.json']:
        if not project_dir.joinpath(f).exists(): errors.append(f"Missing: {f}")
    try:
        with open(project_dir / 'config.json') as c: config = json.load(c)
        if not isinstance(config, dict): errors.append("Invalid config structure")
    except Exception: errors.append("Failed to load config.json")
    return errors

def run_demo():
    print("--- CraftFlow Demo ---")
    for f in ['materials', 'milestones', 'costs', 'inspiration']:
        try:
            with open(Path(__file__).parent / f + '.json') as fp: data = json.load(fp)
            if isinstance(data, list): print(f"[{f}] {len(data)} entries loaded")
        except Exception: pass
    print("--- Demo Complete ---")

if __name__ == "__main__":
    errors = validate_project()
    if errors: sys.exit(1)
    run_demo()
