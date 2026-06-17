# === Stage 34: Add support for multiple local user profiles ===
# Project: CraftFlow
import json, os
from pathlib import Path

class ProfileManager:
    def __init__(self, base_dir):
        self.base = Path(base_dir) / ".profiles"
        self.default_profile = "default.json"
        
    def load_profiles(self):
        profiles_path = self.base / self.default_profile
        if not profiles_path.exists():
            return {"default": {}}
        with open(profiles_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                return {k: v for k, v in data.items() if isinstance(v, dict)}
            except json.JSONDecodeError:
                return {}

    def save_profiles(self, profiles):
        self.base.mkdir(parents=True, exist_ok=True)
        with open(self.base / self.default_profile, 'w', encoding='utf-8') as f:
            json.dump(profiles, f, indent=2, ensure_ascii=False)

    def get_active_profile(self, profile_name=None):
        profiles = self.load_profiles()
        if not profile_name or profile_name == "default":
            return profiles.get("default", {})
        return profiles.get(profile_name, {})

    def set_active_profile(self, name, data):
        profiles = self.load_profiles()
        if name == "default":
            profiles["default"] = data
        else:
            profiles[name] = data
        self.save_profiles(profiles)
