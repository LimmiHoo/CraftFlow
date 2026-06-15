# === Stage 24: Add grouped summaries by category or status ===
# Project: CraftFlow
def group_summaries(data, key_field='category'):
    groups = {}
    for item in data:
        k = item.get(key_field)
        if k is None: continue
        if k not in groups: groups[k] = {'count': 0, 'total_cost': 0.0}
        groups[k]['count'] += 1
        groups[k]['total_cost'] += float(item.get('cost', 0))

    return [{'name': name, **stats} for name, stats in sorted(groups.items())]
