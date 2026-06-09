# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: CraftFlow
class CraftFlowApp:
    def __init__(self):
        self.projects = {}
        self.materials = {}
        self.milestones = {}
        self.costs = {}
        self.inspiration = {}
        
    def add_project(self, name, description):
        if name not in self.projects:
            self.projects[name] = {"name": name, "description": description, "status": "active"}
        return self.projects[name]
    
    def add_material(self, project_name, item, quantity, unit_cost):
        if project_name not in self.materials:
            self.materials[project_name] = []
        self.materials[project_name].append({"item": item, "quantity": quantity, "unit_cost": unit_cost})
        return self.calculate_total_cost(project_name)
    
    def add_milestone(self, project_name, title, date_completed):
        if project_name not in self.milestones:
            self.milestones[project_name] = []
        self.milestones[project_name].append({"title": title, "date_completed": date_completed})
        return len(self.milestones[project_name])
    
    def add_inspiration(self, project_name, note):
        if project_name not in self.inspiration:
            self.inspiration[project_name] = []
        self.inspiration[project_name].append(note)
        return self.inspiration[project_name][-1]
    
    def calculate_total_cost(self, project_name):
        total = 0.0
        if project_name in self.materials:
            for mat in self.materials[project_name]:
                total += mat["quantity"] * mat["unit_cost"]
        return round(total, 2)
    
    def get_project_summary(self, project_name):
        if project_name not in self.projects:
            return None
        summary = {
            "name": self.projects[project_name]["name"],
            "description": self.projects[project_name]["description"],
            "status": self.projects[project_name]["status"],
            "total_cost": self.calculate_total_cost(project_name),
            "milestone_count": len(self.milestones.get(project_name, [])),
            "inspiration_count": len(self.inspiration.get(project_name, []))
        }
        return summary

# Demo dataset initialization
app = CraftFlowApp()
app.add_project("WoodenBird", "Hand-carved wooden bird for home decor")
app.add_material("WoodenBird", "Oak wood", 2.5, 15.0)
app.add_material("WoodenBird", "Paint", 0.5, 8.0)
app.add_milestone("WoodenBird", "Design finalized", "2023-10-01")
app.add_milestone("WoodenBird", "First cut completed", "2023-10-05")
app.add_inspiration("WoodenBird", "Nature's symmetry is perfect.")
print(app.get_project_summary("WoodenBird"))
