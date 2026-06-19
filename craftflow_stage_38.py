# === Stage 38: Add data integrity checks for broken references ===
# Project: CraftFlow
def validate_references(data):
    valid_materials = {m['id'] for m in data.get('materials', [])}
    valid_milestones = {m['id'] for m in data.get('milestones', [])}
    errors = []
    for item in data.get('items', []):
        if item.get('material_id') and item['material_id'] not in valid_materials:
            errors.append(f"Item '{item['name']}' references unknown material {item['material_id']}")
        if item.get('milestone_id') and item['milestone_id'] not in valid_milestones:
            errors.append(f"Item '{item['name']}' references unknown milestone {item['milestone_id']}")
    return errors
