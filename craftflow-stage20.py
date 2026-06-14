# === Stage 20: Add duplicate detection for newly created records ===
# Project: CraftFlow
class DuplicateChecker:
    def __init__(self, db):
        self.db = db
    
    def check_material(self, name, quantity=None):
        query = "SELECT id FROM materials WHERE LOWER(name) = :name"
        result = self.db.execute(query, {"name": name.lower()}).fetchone()
        if result:
            return f"Duplicate material '{name}' found (ID: {result['id']})"
        return None
    
    def check_milestone(self, title):
        query = "SELECT id FROM milestones WHERE LOWER(title) = :title"
        result = self.db.execute(query, {"title": title.lower()}).fetchone()
        if result:
            return f"Duplicate milestone '{title}' found (ID: {result['id']})"
        return None
    
    def check_cost(self, item_name):
        query = "SELECT id FROM costs WHERE LOWER(item) = :item"
        result = self.db.execute(query, {"item": item_name.lower()}).fetchone()
        if result:
            return f"Duplicate cost entry '{item_name}' found (ID: {result['id']})"
        return None
    
    def check_inspiration(self, note):
        query = "SELECT id FROM inspirations WHERE LOWER(note) = :note"
        result = self.db.execute(query, {"note": note.lower()}).fetchone()
        if result:
            return f"Duplicate inspiration '{note}' found (ID: {result['id']})"
        return None
