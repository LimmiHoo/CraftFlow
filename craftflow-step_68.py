# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: CraftFlow
def generate_changelog(activity_log, max_entries=10):
    """Generate a compact changelog from activity log entries."""
    if not activity_log:
        return "No changes recorded."
    
    # Sort by timestamp descending to show newest first
    sorted_logs = sorted(activity_log, key=lambda x: x.get('timestamp', ''), reverse=True)
    truncated_logs = sorted_logs[:max_entries]
    
    changelog_lines = ["# CraftFlow Changelog"]
    
    for entry in truncated_logs:
        date_str = entry.get('date', 'Unknown')
        author = entry.get('author', 'Anonymous')
        message = entry.get('message', '')
        
        if message:
            summary = f"- **{date_str}** by {author}: {message}"
        else:
            summary = f"- **{date_str}** by {author}: [Activity logged]"
            
        changelog_lines.append(summary)
    
    return "\n".join(changelog_lines)
