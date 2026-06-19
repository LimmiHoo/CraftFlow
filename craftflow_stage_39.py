# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: CraftFlow
def repair_data_integrity(data):
    if isinstance(data, list) and len(data) > 0:
        for i in range(len(data)):
            item = data[i]
            if 'materials' in item and item['materials']:
                missing_keys = ['name', 'quantity']
                for key in missing_keys:
                    if key not in item['materials'][0]:
                        item['materials'][0][key] = None
            if 'milestones' in item and item['milestones']:
                for m in item['milestones']:
                    if 'status' not in m:
                        m['status'] = 'pending'
                    if 'date' not in m:
                        m['date'] = None
            if 'costs' in item and item['costs']:
                total_cost = 0.0
                for c in item['costs']:
                    try:
                        float(c.get('amount', 0))
                    except (ValueError, TypeError):
                        c['amount'] = 0.0
                    total_cost += float(c.get('amount', 0))
                if 'total' not in item or abs(item.get('total', 0) - total_cost) > 0.01:
                    item['total'] = round(total_cost, 2)
            if 'inspiration_notes' in item and item['inspiration_notes']:
                for note in item['inspiration_notes']:
                    if not isinstance(note.get('text', ''), str):
                        note['text'] = ''
    return data
