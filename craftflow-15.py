# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: CraftFlow
class CommandDispatcher:
    def __init__(self, handlers):
        self.handlers = {cmd.lower(): handler for cmd, handler in handlers.items()}
    
    def dispatch(self, text_input):
        if not text_input.strip():
            return "No command provided."
        
        parts = text_input.split(maxsplit=1)
        if len(parts) < 1:
            return "Usage: [command] [arguments]"
        
        cmd_name = parts[0].strip()
        args_str = parts[1] if len(parts) > 1 else ""
        
        handler = self.handlers.get(cmd_name.lower())
        if not handler:
            available = ", ".join(self.handlers.keys())
            return f"Unknown command '{cmd_name}'. Available commands: {available}"
        
        try:
            result = handler(args_str)
            return str(result)
        except Exception as e:
            return f"Error executing command: {e}"
