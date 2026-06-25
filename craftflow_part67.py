# === Stage 67: Add a function that returns key project metrics ===
# Project: CraftFlow
def get_project_metrics(project_data):
    """Calculate and return key metrics for a creative project."""
    total_materials_cost = sum(item.get('cost', 0) for item in project_data.get('materials', []))
    total_estimated_cost = total_materials_cost + project_data.get('labor_estimate', 0)
    
    milestones_completed = len([m for m in project_data.get('milestones', []) if m.get('status') == 'completed'])
    total_milestones = len(project_data.get('milestones', []))
    completion_percentage = (milestones_completed / total_milestones * 100) if total_milestones > 0 else 0
    
    inspiration_count = len(project_data.get('inspiration_notes', []))
    
    metrics = {
        'total_materials_cost': round(total_materials_cost, 2),
        'total_estimated_cost': round(total_estimated_cost, 2),
        'milestones_completed': milestones_completed,
        'completion_percentage': round(completion_percentage, 1),
        'inspiration_count': inspiration_count
    }
    
    return metrics
