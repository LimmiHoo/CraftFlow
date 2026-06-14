# === Stage 22: Add favorite records and quick favorite listing ===
# Project: CraftFlow
class FavoriteManager:
    def __init__(self, db_path):
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS favorites (id INTEGER PRIMARY KEY AUTOINCREMENT, record_id TEXT UNIQUE, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

    def add_favorite(self, record_id: str) -> bool:
        try:
            self.cursor.execute("INSERT INTO favorites (record_id) VALUES (?)", (record_id,))
            self.db.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def remove_favorite(self, record_id: str) -> bool:
        self.cursor.execute("DELETE FROM favorites WHERE record_id = ?", (record_id,))
        self.db.commit()
        return self.cursor.rowcount > 0

    def get_favorites(self) -> List[Dict]:
        self.cursor.execute("SELECT id, record_id, created_at FROM favorites ORDER BY created_at DESC")
        rows = self.cursor.fetchall()
        return [{"id": r[0], "record_id": r[1], "created_at": r[2]} for r in rows]

    def close(self):
        self.db.close()
