# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: CraftFlow
def sort_projects(criteria='date'):
    valid_criteria = ['title', 'date', 'priority', 'last_update']
    if criteria not in valid_criteria:
        criteria = 'date'
    reverse_order = {'priority': True, 'date': False, 'title': False, 'last_update': False}
    return sorted(projects, key=lambda x: getattr(x, criteria), reverse=reverse_order.get(criteria))
