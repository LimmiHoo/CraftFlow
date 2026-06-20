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
