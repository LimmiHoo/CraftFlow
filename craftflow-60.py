# === Stage 60: Add saved views for frequently used filters ===
# Project: CraftFlow
class SavedViewManager:
    def __init__(self, db):
        self.db = db

    def save_view(self, name, filters=None, sort_by='created_at'):
        if filters is None:
            filters = {}
        query = f"""
            INSERT INTO saved_views (name, filters_json, sort_by)
            VALUES (:name, :filters, :sort_by)
            ON CONFLICT(name) DO UPDATE SET 
                filters_json=EXCLUDED.filters_json,
                sort_by=EXCLUDED.sort_by
        """
        self.db.execute(query, name=name, filters=filters, sort_by=sort_by)

    def get_saved_views(self):
        query = "SELECT id, name, filters_json, sort_by FROM saved_views ORDER BY created_at DESC"
        return self.db.fetch_all(query)

    def load_view(self, view_id):
        query = "SELECT filters_json, sort_by FROM saved_views WHERE id=:id"
        result = self.db.fetch_one(query, id=view_id)
        if not result:
            raise ValueError(f"Saved view with id {view_id} not found")
        return {'filters': json.loads(result['filters_json']), 'sort_by': result['sort_by']}

    def delete_view(self, name):
        query = "DELETE FROM saved_views WHERE name=:name"
        self.db.execute(query, name=name)
