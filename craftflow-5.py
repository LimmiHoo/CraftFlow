# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: CraftFlow
def update_record(record_id, updates):
    """
    Updates an existing record by ID.
    Handles missing records gracefully by returning a specific error message.
    Only specified fields in 'updates' are modified.
    Returns the updated dictionary or an error string.
    """
    if record_id not in records:
        return f"Error: Record with id '{record_id}' not found."

    current_record = records[record_id].copy()
    
    for key, value in updates.items():
        if key in current_record:
            current_record[key] = value
        else:
            return f"Error: Field '{key}' does not exist in record {record_id}."

    # Optional: Log the update or persist to disk here if needed
    # For now, we keep it in memory as per dependency-free requirement
    
    return current_record
