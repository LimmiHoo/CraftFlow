# === Stage 87: Add small helper functions for comparing two exported reports ===
# Project: CraftFlow
def compare_reports(r1, r2):
    """Compare two CraftFlow reports and return a summary of differences."""
    diffs = []
    if set(r1.keys()) != set(r2.keys()):
        diffs.append(f"Keys differ: {set(r1.keys()).symmetric_difference(set(r2.keys()))}")
    for key in r1.keys():
        v1, v2 = r1[key], r2.get(key)
        if isinstance(v1, list) and isinstance(v2, list):
            set_v1, set_v2 = set(tuple(x.items()) if isinstance(x, dict) else (x,) for x in v1), \
                             set(tuple(x.items()) if isinstance(x, dict) else (x,) for x in v2)
            diffs.append(f"{key}: {set_v1.symmetric_difference(set_v2)}")
        elif v1 != v2:
            diffs.append(f"{key}: {v1!r} vs {v2!r}")
    return sorted(diffs) if diffs else ["Reports are identical"]

def export_diff_summary(r1, r2):
    """Generate a human-readable diff summary for two reports."""
    lines = ["=== CraftFlow Report Comparison ===", ""]
    diffs = compare_reports(r1, r2)
    if not diffs:
        lines.append("No differences found.")
    else:
        lines.append(f"Found {len(diffs)} difference(s):")
        for d in diffs[:5]:  # Limit to first 5 for readability
            lines.append(f"- {d}")
        if len(diffs) > 5:
            lines.append(f"... and {len(diffs)-5} more.")
    return "\n".join(lines)
