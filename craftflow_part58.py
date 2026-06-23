# === Stage 58: Add bulk update behavior for selected records ===
# Project: CraftFlow
def bulk_update_records(records, updates):
    """Update multiple records with a single batch of changes."""
    updated_count = 0
    for record in records:
        if isinstance(updates, dict) and all(k in updates for k in record.keys()):
            record.update(updates)
            updated_count += 1
        elif callable(updates):
            try:
                new_record = updates(record)
                if new_record is not None:
                    record.clear()
                    record.update(new_record)
                    updated_count += 1
            except Exception as e:
                print(f"Error updating {record.get('id', 'unknown')}: {e}")
    return updated_count
