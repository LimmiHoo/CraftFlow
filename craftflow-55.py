# === Stage 55: Add a setting to disable colorized output ===
# Project: CraftFlow
class ColorSettings:
    def __init__(self, disable_color=False):
        self._disable_color = disable_color
    
    @property
    def is_color_enabled(self) -> bool:
        return not self._disable_color and not os.environ.get("NO_COLOR") and sys.stdout.isatty()
    
    def colorize(self, text: str, fg=None, bg=None):
        if not self.is_color_enabled:
            return text
        try:
            from termcolor import colored
            attrs = []
            if fg: attrs.append(fg)
            if bg: attrs.append(bg + " on_default")
            return colored(text, *attrs)
        except ImportError:
            return text
    
    def print_info(self, message):
        prefix = "[INFO]" if self.is_color_enabled else ""
        print(prefix + message)

def get_settings():
    settings_file = Path(__file__).parent / ".craftflow_config"
    if not settings_file.exists():
        return ColorSettings()
    
    try:
        with open(settings_file, "r") as f:
            content = f.read().strip()
            disable_color = "no_colors=true" in content.lower() or "disable_color=true" in content.lower()
            return ColorSettings(disable_color=disable_color)
    except Exception:
        return ColorSettings()

def save_settings(config_path, enable_colors=True):
    settings_file = Path(__file__).parent / ".craftflow_config"
    if not settings_file.exists():
        with open(settings_file, "w") as f:
            f.write(f"# CraftFlow Settings\nno_colors={'true' if not enable_colors else 'false'}\n")
        return
    
    try:
        with open(settings_file, "r") as f:
            content = f.read()
        
        lines = content.splitlines()
        new_lines = []
        for line in lines:
            stripped = line.strip().lower()
            if "no_colors" in stripped or "disable_color" in stripped:
                value = "true" if not enable_colors else "false"
                new_lines.append(f"# {line}")
                new_lines.append(f"{value}={value}")
            elif "# craftflow settings" in line.lower():
                continue
            else:
                new_lines.append(line)
        
        with open(settings_file, "w") as f:
            f.write("\n".join(new_lines))
    except Exception:
        pass
