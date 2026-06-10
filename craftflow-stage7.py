# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: CraftFlow
def format_list(items, prefix="  -"):
    """Compact list formatter for console output."""
    if not items:
        return "  (none)"
    lines = [f"{prefix}{item}" for item in items]
    return "\n".join(lines)

def format_detail(title, data):
    """Format key-value pairs into a readable block."""
    if not data:
        return ""
    lines = [f"\n{title}:"]
    for key, value in data.items():
        lines.append(f"  {key}: {value}")
    return "\n".join(lines)

def format_summary(project):
    """Generate a compact summary block for console display."""
    output = []
    output.append("=" * 40)
    output.append(f"Project: {project.get('name', 'Unknown')}")
    output.append(f"Status: {project.get('status', 'N/A')}")
    if project.get('materials'):
        output.append("Materials:")
        output.extend(format_list(project['materials']))
    if project.get('milestones'):
        output.append("Milestones:")
        output.extend(format_list(project['milestones']))
    if project.get('costs'):
        output.append("Costs:")
        output.extend(format_list(project['costs'], prefix="  $"))
    if project.get('inspiration'):
        output.append("Inspiration:")
        output.append(f"  {project['inspiration']}")
    output.append("=" * 40)
    return "\n".join(output)
