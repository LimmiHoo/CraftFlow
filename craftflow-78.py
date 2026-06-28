# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: CraftFlow
def split_project_costs(total_cost, materials_list):
    if total_cost <= 0:
        return []
    cost_per_item = total_cost / len(materials_list)
    return [(item, round(cost_per_item, 2)) for item in materials_list]

def format_milestone(milestones_data):
    formatted = []
    for milestone_id, details in milestones_data.items():
        entry = {
            "id": milestone_id,
            "title": details.get("title", ""),
            "status": details.get("status", "pending"),
            "date": details.get("date", "")
        }
        formatted.append(entry)
    return sorted(formatted, key=lambda x: x["id"])

def enrich_inspiration_notes(raw_notes):
    enriched = []
    for note_id, content in raw_notes.items():
        entry = {
            "source": content.get("source", "unknown"),
            "tags": [tag.strip() for tag in content.get("tags", "").split(",") if tag.strip()],
            "text": content.get("text", "")
        }
        enriched.append(entry)
    return sorted(enriched, key=lambda x: x["source"])

def validate_project_entry(project_data):
    required_fields = ["name", "creator"]
    missing = [field for field in required_fields if not project_data.get(field)]
    is_valid = len(missing) == 0
    return {
        "valid": is_valid,
        "missing_fields": missing,
        "data": project_data if is_valid else None
    }

def generate_project_summary(project_name, creator, total_cost):
    summary_lines = [f"Project: {project_name}", f"Creator: {creator}"]
    if total_cost > 0:
        summary_lines.append(f"Estimated Cost: ${total_cost:.2f}")
    return "\n".join(summary_lines)
