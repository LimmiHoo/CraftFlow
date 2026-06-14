# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: CraftFlow
def manage_tags(tags: dict, item_id: str) -> tuple[dict, list[str]]:
    if "tags" not in tags: tags["tags"] = {}
    current_tags = tags.get("tags", {}).get(item_id, [])
    action_type = sys.argv[-1] if len(sys.argv) > 1 else None
    if action_type == "add": new_tag = input(f"Enter tag for {item_id}: ").strip()
    elif action_type == "remove": new_tag = input(f"Remove which tag from {item_id}? ").strip()
    else: return tags, []
    if not new_tag: return tags, []
    current_tags_set = set(current_tags)
    if action_type == "add" and new_tag in current_tags_set: print("Tag already exists.")
    elif action_type == "remove" and new_tag not in current_tags_set: print(f"Tag '{new_tag}' not found.")
    else:
        if action_type == "add": current_tags.append(new_tag)
        else: current_tags.remove(new_tag)
        tags["tags"][item_id] = sorted(current_tags)
    summary_lines = [f"{item_id}: {', '.join(tags['tags'].get(item_id, []))}"]
    return tags, summary_lines
