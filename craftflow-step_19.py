# === Stage 19: Add undo support for the last simple mutation ===
# Project: CraftFlow
import json
from typing import Optional, List, Dict, Any
from datetime import datetime

class CraftFlow:
    def __init__(self):
        self.history: List[Dict[str, Any]] = []
    
    def _save_state(self) -> None:
        state = {
            "history": self.history.copy(),
            "timestamp": datetime.now().isoformat()
        }
        with open("craftflow_state.json", "w") as f:
            json.dump(state, f)

class UndoManager:
    def __init__(self, craft_flow: CraftFlow):
        self.craft_flow = craft_flow
    
    def undo_last(self) -> Optional[Dict[str, Any]]:
        if not self.craft_flow.history:
            return None
        
        last_state = self.craft_flow.history[-1]
        del self.craft_flow.history[-1]
        
        # Restore state from history snapshot
        restored_data = json.loads(last_state.get("data", "{}"))
        for key, value in restored_data.items():
            setattr(self.craft_flow, key, value)
        
        return last_state
