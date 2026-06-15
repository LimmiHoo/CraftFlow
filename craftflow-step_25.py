# === Stage 25: Add daily summary calculations ===
# Project: CraftFlow
def calculate_daily_summary(records):
    from collections import defaultdict
    daily_costs = defaultdict(float)
    daily_materials = defaultdict(list)
    for rec in records:
        if 'date' in rec and 'cost' in rec:
            key = rec['date'][:10]
            daily_costs[key] += float(rec.get('cost', 0))
            if 'material' in rec:
                daily_materials[key].append(rec['material'])
    summary = []
    for date, cost in sorted(daily_costs.items()):
        materials_str = ', '.join(sorted(set(daily_materials[date]))) if daily_materials[date] else '-'
        summary.append(f"{date}: Cost={cost:.2f}, Materials=[{materials_str}]")
    return '\n'.join(summary)
