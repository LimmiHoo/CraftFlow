# === Stage 40: Add plain text report export ===
# Project: CraftFlow
def export_report(project_data, output_file="report.txt"):
    with open(output_file, "w", encoding="utf-8") as f:
        for name, data in project_data.items():
            f.write(f"=== {name} ===\n")
            if "materials" in data:
                f.write("Materials:\n")
                for mat in data["materials"]:
                    cost = float(mat.get("cost", 0))
                    f.write(f" - {mat['item']}: {mat['quantity']}x ${cost:.2f}\n")
            if "milestones" in data:
                f.write("\nMilestones:\n")
                for m in sorted(data["milestones"], key=lambda x: x.get("date", "")):
                    status = "[✓]" if m.get("done") else "[ ]"
                    f.write(f"{status} {m['title']} ({m.get('date', 'N/A')})\n")
            if "costs" in data:
                total_cost = sum(float(c) for c in data["costs"].values())
                f.write(f"\nTotal Cost: ${total_cost:.2f}\n")
            if "inspiration" in data and data["inspiration"]:
                f.write("\nInspiration Notes:\n")
                for note in data["inspiration"]:
                    f.write(f"- {note['source']}: \"{note['text']}\"\n")
