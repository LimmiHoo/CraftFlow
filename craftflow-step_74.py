# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: CraftFlow
def compare_snapshots(before: dict, after: dict) -> list[str]:
    """Generate a human-readable diff between two project state snapshots."""
    changes = []
    all_keys = set(before.keys()) | set(after.keys())
    for key in sorted(all_keys):
        b_val = before.get(key)
        a_val = after.get(key)
        if key not in before:
            changes.append(f"+ {key}: {a_val}")
        elif key not in after:
            changes.append(f"- {key}: {b_val}")
        elif type(b_val) != type(a_val):
            changes.append(f"~ {key} changed type: {type(b_val).__name__} -> {type(a_val).__name__}")
        else:
            if b_val != a_val:
                changes.append(f"* {key}: '{b_val}' -> '{a_val}'")
    return changes
