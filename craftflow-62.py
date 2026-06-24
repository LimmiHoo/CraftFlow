# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: CraftFlow
class PriorityCalculator:
    def __init__(self, materials, milestones):
        self.materials = materials
        self.milestones = milestones
    
    def calculate_priority(self, item_type='milestone'):
        score_map = {'material': 0.5, 'milestone': 1.2}
        weights = {
            'urgency': lambda x: (x['deadline'] - datetime.now()).days if isinstance(x.get('deadline'), str) else 365,
            'impact': lambda x: x.get('importance', 0),
            'cost_efficiency': lambda x: x.get('estimated_cost', 0) / max(1, self.materials.get_total_value())
        }
        
        def get_score(item):
            base = score_map.get(item_type, 0.8) * item.get('importance', 5)
            urgency_factor = weights['urgency'](item) / 365 if isinstance(weights['urgency'](item), int) else 1.0
            cost_penalty = min(1.0, max(0.5, 1 - (weights['cost_efficiency'](item) * 2)))
            return base * urgency_factor * cost_penalty
        
        items_to_score = self.milestones if item_type == 'milestone' else self.materials.items()
        
        scored_items = []
        for idx, item in enumerate(items_to_score):
            score = get_score(item)
            priority_rank = sum(1 for i in items_to_score if get_score(i) > score) + 1
            status = 'High' if priority_rank <= 3 else ('Medium' if priority_rank <= 6 else 'Low')
            
            scored_items.append({
                **item,
                'calculated_priority': round(score, 2),
                'priority_status': status
            })
        
        return sorted(scored_items, key=lambda x: x['calculated_priority'], reverse=True)
