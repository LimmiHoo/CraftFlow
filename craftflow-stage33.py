# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: CraftFlow
CRAFT_FLOW_SETTINGS = {
    "currency": "USD",
    "date_format": "%Y-%m-%d",
    "default_material_qty": 1,
    "backup_dir": "./backups"
}

def update_settings(key: str, value):
    if key in CRAFT_FLOW_SETTINGS:
        CRAFT_FLOW_SETTINGS[key] = value
        return True
    raise KeyError(f"Unknown setting: {key}")

def get_setting(key: str, default=None):
    return CRAFT_FLOW_SETTINGS.get(key, default)
