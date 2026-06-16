# === Stage 28: Add overdue item detection based on due dates ===
# Project: CraftFlow
from datetime import date, timedelta
def check_overdue_items(items):
    today = date.today()
    overdue_list = []
    for item in items:
        due_date_str = item.get('due_date', '')
        if not due_date_str: continue
        try:
            due_date = date.fromisoformat(due_date_str)
            days_overdue = (today - due_date).days
            if days_overdue > 0:
                status = 'overdue'
                item['status'] = status
                item['days_overdue'] = days_overdue
                overdue_list.append(item.copy())
        except ValueError:
            pass
    return overdue_list
