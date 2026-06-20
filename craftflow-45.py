# === Stage 45: Add restore from backup with validation ===
# Project: CraftFlow
import json, os, hashlib

def restore_backup(backup_file: str, target_dir: str) -> bool:
    if not backup_file.endswith('.json'):
        raise ValueError("Backup must be a JSON file")
    
    try:
        with open(backup_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        required_keys = {'projects', 'materials', 'milestones'}
        if not all(k in data for k in required_keys):
            raise ValueError("Backup structure is invalid")
        
        backup_hash = hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()[:16]
        target_path = os.path.join(target_dir, 'craftflow_backup.json')
        
        with open(target_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        
        print(f"Restored from {backup_file} (hash: {backup_hash})")
        return True
        
    except FileNotFoundError:
        raise ValueError("Backup file not found")
