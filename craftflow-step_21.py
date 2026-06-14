# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: CraftFlow
from datetime import datetime, timedelta
import json
import os

ARCHIVE_DIR = "archive"
DAYS_TO_ARCHIVE = 365

def archive_old_records(data):
    cutoff_date = datetime.now() - timedelta(days=DAYS_TO_ARCHIVE)
    archived_items = []
    remaining_data = {}
    
    for key, record in data.items():
        if isinstance(record.get('completed_at'), str):
            completed_dt = datetime.fromisoformat(record['completed_at'])
        else:
            completed_dt = record.get('completed_at') or datetime.now()
            
        if completed_dt < cutoff_date and not record.get('is_active', True):
            archived_items.append((key, record))
            continue
            
        remaining_data[key] = record
        
    for key, record in archived_items:
        filename = f"{ARCHIVE_DIR}/{datetime.fromtimestamp(record['created_at']).strftime('%Y%m%d')}.json"
        os.makedirs(ARCHIVE_DIR, exist_ok=True)
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump([record], f, indent=2, ensure_ascii=False)

def restore_from_archive(data):
    if not os.path.exists(ARCHIVE_DIR):
        return data
        
    archived_files = sorted(os.listdir(ARCHIVE_DIR))
    
    for filename in archived_files:
        filepath = os.path.join(ARCHIVE_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            records = json.load(f)
            
        for record in records:
            key = f"archived_{filename}"
            if key not in data:
                data[key] = record
                
    return data
