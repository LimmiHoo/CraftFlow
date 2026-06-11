# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: CraftFlow
def filter_projects(projects, status=None, category=None, owner=None, tag=None):
    filtered = []
    for p in projects:
        if status and p.get('status') != status:
            continue
        if category and p.get('category') != category:
            continue
        if owner and p.get('owner') != owner:
            continue
        if tag and tag not in p.get('tags', []):
            continue
        filtered.append(p)
    return filtered

def search_projects(projects, query=None):
    if not query:
        return projects
    q = query.lower()
    results = []
    for p in projects:
        text = f"{p.get('name', '')} {p.get('description', '')} {p.get('tags', [])}".lower()
        if q in text:
            results.append(p)
    return results

def get_projects_by_owner(projects, owner):
    return [p for p in projects if p.get('owner') == owner]

def get_projects_by_category(projects, category):
    return [p for p in projects if p.get('category') == category]

def get_projects_by_status(projects, status):
    return [p for p in projects if p.get('status') == status]

def get_projects_by_tag(projects, tag):
    return [p for p in projects if tag in p.get('tags', [])]
