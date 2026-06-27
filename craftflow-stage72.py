# === Stage 72: Add Markdown report export ===
# Project: CraftFlow
def export_report(project_data, output_path="report.md"):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# CraftFlow Project Report\n")
        for name, data in project_data.items():
            f.write(f"\n## {name}\n")
            if "materials" in data:
                f.write("| Material | Qty | Cost |\n|---|---|---|\n")
                for mat in data["materials"]:
                    f.write(f"| {mat['name']} | {mat.get('qty', '?')} | ${mat.get('cost', 0):.2f} |\n")
            if "milestones" in data:
                f.write("\n### Milestones\n")
                for m in data["milestones"]:
                    status = "[x]" if m.get("done", False) else "[ ]"
                    f.write(f"- {status} **{m['title']}**: {m.get('notes', '')}\n")
            if "inspiration" in data:
                f.write("\n### Inspiration\n> " + data["inspiration"].replace("|", "\\|"))
