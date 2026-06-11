# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: CraftFlow
class SearchFilter:
    def __init__(self, data):
        self.data = data
    
    def search(self, query, fields=None):
        if not fields:
            fields = ['name', 'material', 'note']
        query_lower = query.lower().strip()
        results = []
        for item in self.data:
            match = False
            for field in fields:
                val = str(item.get(field, '')).lower()
                if query_lower in val:
                    match = True
                    break
            if match:
                results.append(item)
        return results

if __name__ == "__main__":
    projects = [
        {"id": 1, "name": "Wooden Chair", "material": "Oak wood", "note": "Classic design"},
        {"id": 2, "name": "Glass Table", "material": "Tempered glass", "note": "Modern look"},
        {"id": 3, "name": "Ceramic Vase", "material": "Clay", "note": "Handmade pottery"}
    ]
    
    # Case-insensitive search for 'glass' in name or material
    filter_obj = SearchFilter(projects)
    found = filter_obj.search("GLASS")
    print(f"Found {len(found)} items:")
    for p in found:
        print(p['name'])
