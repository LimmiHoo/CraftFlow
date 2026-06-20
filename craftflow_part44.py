# === Stage 44: Add backup creation for the data file ===
# Project: CraftFlow
import shutil, os, datetime
BACKUP_DIR = "backups"
os.makedirs(BACKUP_DIR, exist_ok=True)
def create_backup(data_file):
    if not data_file: return
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(BACKUP_DIR, f"{data_file.split('/')[-1]}.{timestamp}")
    shutil.copy2(data_file, backup_path)
    print(f"Backup created: {backup_path}")

# Usage example within main script logic
if __name__ == "__main__":
    create_backup("projects.json")

# === Stage 44: Add backup creation for the data file ===
# Project: CraftFlow
import os, json, datetime, hashlib, shutil
from pathlib import Path

def backup_data(data_file: str, backup_dir: str = "backups") -> None:
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_hash = hashlib.md5(open(data_file, 'rb').read()).hexdigest()[:8]
    backup_name = f"{os.path.basename(data_file)}.v{file_hash}_{timestamp}.json"
    backup_path = os.path.join(backup_dir, backup_name)
    shutil.copy2(data_file, backup_path)
