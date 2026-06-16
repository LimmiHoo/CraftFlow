# === Stage 27: Add monthly summary calculations ===
# Project: CraftFlow
def calculate_monthly_summary(data):
    from collections import defaultdict
    monthly_costs = defaultdict(float)
    monthly_materials = defaultdict(list)
    for item in data:
        month_key = f"{item['month']} {item['year']}"
        if 'cost' in item and item['cost']:
            monthly_costs[month_key] += float(item['cost'])
        if 'materials' in item and item['materials']:
            monthly_materials[month_key].extend(item['materials'])
    summary = []
    for month, cost in sorted(monthly_costs.items()):
        materials_str = "; ".join(set(materials)) if monthly_materials.get(month) else "None"
        summary.append(f"{month}: Cost={cost:.2f}, Materials=[{materials_str}]")
    return "\n".join(summary)
