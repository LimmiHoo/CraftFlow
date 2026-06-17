# === Stage 31: Add compact table rendering for long lists ===
# Project: CraftFlow
def render_compact_table(items, columns):
    """Render a compact table for long lists with word wrapping."""
    if not items: return ""
    widths = [max(len(str(item[i])) for item in items) + 2 for i in range(len(columns))]
    header = " | ".join(w.center(widths[i]) for i, w in enumerate(columns))
    line = "-" * len(header)
    rows = []
    for item in items:
        row_parts = [str(item.get(col, ""))[:widths[i]-2] if isinstance(item.get(col), str) else str(item[col]) for i, col in enumerate(columns)]
        rows.append(" | ".join(row_parts).ljust(len(header)))
    return "\n".join([header, line] + rows)
