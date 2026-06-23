# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: CraftFlow
class BulkDeleteGuard:
    def __init__(self, db):
        self.db = db
        self.confirm_flag = False

    def set_confirm(self, value: bool) -> None:
        """Enable or disable the bulk delete confirmation requirement."""
        self.confirm_flag = value

    async def execute_bulk_delete(self, table_name: str, where_clause: dict) -> int | None:
        if not self.confirm_flag:
            return None
        
        try:
            query = f"DELETE FROM {table_name} WHERE ({' AND '.join(f'{k}=?' for k in where_clause.keys())})"
            params = list(where_clause.values())
            
            async with self.db.acquire() as conn:
                result = await conn.execute(query, *params)
                return int(result) if hasattr(result, 'rowcount') else 1
                
        except Exception as e:
            raise RuntimeError(f"Bulk delete failed for {table_name}: {e}")
