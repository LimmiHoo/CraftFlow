# === Stage 42: Add CSV export without external dependencies ===
# Project: CraftFlow
def export_to_csv(projects, filename="craftflow_export.csv"):
    import csv
    if not projects: return False
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "materials", "milestones", "costs", "inspiration"])
        writer.writeheader()
        for p in projects:
            writer.writerow({
                "name": p.get("name"),
                "materials": "; ".join(p.get("materials", [])),
                "milestones": "; ".join(p.get("milestones", [])),
                "costs": str(sum(float(c) for c in p.get("costs", []))),
                "inspiration": p.get("inspiration") or ""
            })
    return True
