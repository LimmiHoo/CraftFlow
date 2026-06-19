# === Stage 41: Add plain text import for a simple line-based format ===
# Project: CraftFlow
def load_text_projects(path):
    projects = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split('|||')
            if len(parts) == 5:
                name, desc, mat, cost, insp = parts
                projects.append({
                    "name": name,
                    "description": desc,
                    "materials": mat.split('; ') if ';' in mat else [mat],
                    "cost": float(cost.replace('$', '').replace(',', '')) if cost else 0.0,
                    "inspiration": insp
                })
    return projects

def save_text_projects(projects, path):
    with open(path, 'w', encoding='utf-8') as f:
        for p in projects:
            mat_str = '; '.join(p['materials'])
            cost_str = f"${p['cost']:.2f}" if p['cost'] > 0 else "N/A"
            line = f"{p['name']}|||{p['description']}|||{mat_str}|||{cost_str}|||{p['inspiration']}\n"
            f.write(line)

if __name__ == "__main__":
    import json, os
    data_file = "craftflow_data.json"
    text_file = "craftflow_projects.txt"
    
    if not os.path.exists(data_file):
        print("No JSON data found. Skipping merge.")
    else:
        try:
            with open(data_file) as f:
                json_data = json.load(f)
            
            loaded = load_text_projects(text_file)
            
            all_projects = []
            for proj in loaded + json_data.get('projects', []):
                if not any(p['name'] == proj['name'] for p in all_projects):
                    all_projects.append(proj)
            
            merged_json = {"version": "41", "count": len(all_projects), "projects": all_projects}
            save_text_projects(merged_json.get('projects', []), text_file)
            
            with open(data_file, 'w') as f:
                json.dump(merged_json, f, indent=2)
                
        except Exception as e:
            print(f"Error merging projects: {e}")
