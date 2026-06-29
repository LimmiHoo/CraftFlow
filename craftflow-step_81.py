# === Stage 81: Add final README text as a module string with usage examples ===
# Project: CraftFlow
def get_usage_examples():
    """Returns a formatted string with usage examples for CraftFlow."""
    return '''
# Usage Examples

## 1. Create and Save Project Data
from craftflow import Project, Material, Milestone, Cost, Inspiration

project = Project("Wooden Chair", "Furniture")

material = Material(name="Oak Wood", quantity=20, unit="board feet", cost_per_unit=45.0)
milestone = Milestone(title="Frame Assembly", completed=False, date_due="2023-12-31")
cost_entry = Cost(category="Materials", amount=900.0, description="Oak wood purchase")
inspiration_note = Inspiration(source="Pinterest Board #452", url="https://pinterest.com/...", text="Minimalist design focus.")

project.add_material(material)
project.add_milestone(milestone)
project.add_cost(cost_entry)
project.add_inspiration(inspiration_note)

# Save to JSON file (no external dependencies required)
with open("chair_project.json", "w") as f:
    project.save(f)

## 2. Load and Display Project Summary
import json

with open("chair_project.json", "r") as f:
    data = json.load(f)

project = Project.from_dict(data)

print(f"Project: {project.name}")
for mat in project.materials:
    print(f"- Material: {mat.name} ({mat.quantity} {mat.unit}) - Cost: ${mat.total_cost:.2f}")
for mil in project.milestones:
    status = "Done" if mil.completed else "Pending"
    print(f"- Milestone: {mil.title} [{status}]")

## 3. Calculate Total Estimated Cost
total_materials = sum(m.total_cost for m in project.materials)
total_costs = sum(c.amount for c in project.costs)
estimated_total = total_materials + total_costs
print(f"Total Estimated Cost: ${estimated_total:.2f}")

'''
