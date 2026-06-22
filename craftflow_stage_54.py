# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: CraftFlow
def colorize(text, style='default'):
    codes = {
        'red': '\x1b[31m', 'green': '\x1b[32m', 'yellow': '\x1b[33m',
        'blue': '\x1b[34m', 'cyan': '\x1b[36m', 'bold': '\x1b[1m',
        'reset': '\x1b[0m'
    }
    if style in codes: return f"{codes.get(style, '')}{text}{codes['reset']}"
    elif isinstance(text, str): return text
    else: return repr(text)

def print_report(materials=None, milestones=None, costs=None, notes=None):
    print(colorize("=== CRAFTFLOW REPORT ===", 'bold'))
    if materials:
        for mat in materials:
            status = colorize('✓', 'green') if mat['done'] else colorize('○', 'yellow')
            print(f"{status} {mat['name']} ({mat['qty']} units)")
    if milestones:
        for ms in milestones:
            print(colorize(f"\n--- Milestone: {ms['title']} ---", 'cyan'))
            print(f"  Date: {ms.get('date', 'N/A')}")
            print(f"  Status: {'Done' if ms.get('done') else colorize('In Progress', 'yellow')}")
    if costs:
        total = sum(c['amount'] for c in costs)
        print(colorize(f"\nTotal Cost: ${total:.2f}", 'red'))
    if notes:
        for note in notes:
            tag = colorize(note.get('tag', ''), 'blue')
            print(f"{tag} {note['text']}")
    else:
        print("\nNo inspiration notes added yet.")

if __name__ == "__main__":
    sample_materials = [{'name': 'Wood', 'qty': 5, 'done': True}, {'name': 'Glue', 'qty': 1, 'done': False}]
    sample_milestones = [{'title': 'Design Phase', 'date': '2023-10-01', 'done': True}]
    sample_costs = [{'amount': 45.99}, {'amount': 12.50}]
    sample_notes = [{'text': 'Use dark oak for contrast.', 'tag': 'Tip'}, {'text': 'Remember to sand edges.', 'tag': 'Warning'}]
    print_report(materials=sample_materials, milestones=sample_milestones, costs=sample_costs, notes=sample_notes)
