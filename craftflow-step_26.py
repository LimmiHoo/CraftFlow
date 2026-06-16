# === Stage 26: Add weekly summary calculations ===
# Project: CraftFlow
def calculate_weekly_summary(projects, start_date):
    from datetime import timedelta
    current = start_date + timedelta(days=7)
    total_cost = 0.0
    completed_milestones = []
    for proj in projects:
        if proj['status'] == 'active':
            cost_delta = min(proj.get('budget', {}).get('spent', 0), proj['end_date']) - max(0, current)
            total_cost += cost_delta
            for milestone in proj.get('milestones', []):
                if milestone['date'] <= current and not milestone['completed']:
                    completed_milestones.append(f"{proj['name']}:{milestone['title']}")
    return {'total_spent': round(total_cost, 2), 'finished_this_week': completed_milestones}
