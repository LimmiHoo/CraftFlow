# === Stage 43: Add CSV import for the primary record type ===
# Project: CraftFlow
import csv, json, sys
from pathlib import Path
def load_csv(source: str) -> list[dict]:
    path = Path(source).resolve()
    if not path.exists(): raise FileNotFoundError(f"CSV not found: {path}")
    records = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                rec = {'id': int(row.get('id', 0)), 'type': row.get('type', ''), **{k.strip(): v.strip() for k, v in row.items() if k != 'id'}}
                records.append(rec)
            except (ValueError, KeyError):
                continue
    return records

def merge_csv_to_json(csv_path: str, json_db_path: str = "data.json"):
    db = []
    try:
        with open(json_db_path, encoding='utf-8') as f:
            db = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    new_records = load_csv(csv_path)
    for rec in new_records:
        if not any(r.get('id') == rec['id'] and r.get('type') == rec['type'] for r in db):
            db.append(rec)
    with open(json_db_path, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py input.csv [output.json]")
        sys.exit(1)
    merge_csv_to_json(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "data.json")
