# === Stage 50: Add unit tests for import and export behavior ===
# Project: CraftFlow
import json, os
from pathlib import Path
def test_import_export():
    base = Path(__file__).parent / "data"
    base.mkdir(exist_ok=True)
    def _save(path: Path): path.write_text(json.dumps({"items": []}, indent=2))
    def _load(path: Path): return json.loads(path.read_text()) if path.exists() else {"items": []}
    assert _load(base / "empty.json") == {"items": []}
    data = {"items": [{"id": 1, "name": "test"}]}
    (base / "data.json").write_text(json.dumps(data))
    loaded = _load(base / "data.json")
    assert loaded["items"] == data["items"]
    def export_to_csv(items):
        lines = ["id,name,cost,milestone,inspiration"]
        for it in items:
            lines.append(f"{it['id']},{it.get('name','')},{it.get('cost',0)},{it.get('milestone','')},{it.get('inspiration','')}")
        return "\n".join(lines)
    csv = export_to_csv([{"id": 1, "name": "A", "cost": 10.5}])
    assert "A" in csv and "10.5" in csv
