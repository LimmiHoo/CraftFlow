# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: CraftFlow
def validate_project(project: dict) -> list[dict]:
    warnings = []
    errors = []
    if project.get("materials") and isinstance(project["materials"], list):
        for i, mat in enumerate(project["materials"]):
            if not mat.get("quantity", 0) > 0:
                errors.append({"line": i + 1, "msg": f"Material {mat.get('name', 'unknown')} has invalid quantity"})
    if project.get("milestones") and isinstance(project["milestones"], list):
        for i, ms in enumerate(project["milestones"]):
            if not ms.get("completed", False) or not ms.get("due_date"):
                warnings.append({"line": i + 1, "msg": f"Milestone {ms.get('name', 'unknown')} missing completion status or due date"})
    if project.get("costs") and isinstance(project["costs"], dict):
        total = sum(c.get("amount", 0) for c in project["costs"].values())
        declared_total = project.get("total_budget", 0)
        if abs(total - declared_total) > 1.0:
            warnings.append({"line": "budget_summary", "msg": f"Calculated cost {total:.2f} differs from declared budget {declared_total}"})
    return {"errors": errors, "warnings": warnings}
