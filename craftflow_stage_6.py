# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: CraftFlow
def delete_entry(entry_id, confirm_flag=False):
    if not confirm_flag:
        print(f"Warning: No confirmation provided for deleting entry {entry_id}. Operation aborted.")
        return False
    
    try:
        # Assuming 'entries' is a global list or accessible dataset in the scope
        # Find and remove the specific entry by ID
        initial_count = len(entries)
        entries = [e for e in entries if e['id'] != entry_id]
        
        if len(entries) == initial_count:
            print(f"Error: Entry with ID {entry_id} not found.")
            return False
        
        # Optional: Log deletion or update a history file here if needed
        print(f"Entry {entry_id} successfully deleted.")
        return True
    except Exception as e:
        print(f"Error during deletion of entry {entry_id}: {e}")
        return False
