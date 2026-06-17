# === Stage 32: Add pagination helpers for long console output ===
# Project: CraftFlow
def paginate_output(lines, max_lines=15):
    if len(lines) <= max_lines:
        return "\n".join(lines)
    result = []
    for i in range(0, len(lines), max_lines):
        chunk = lines[i:i+max_lines]
        header = f"[Page {i//max_lines + 1}]" if i > 0 else ""
        footer = "\n... (output truncated)" if i + max_lines < len(lines) else ""
        result.append(header)
        result.extend(chunk)
        result.append(footer)
    return "\n".join(result).strip()

def format_table(headers, rows):
    col_widths = [max(len(str(h)), max((len(str(r)) for r in row), default=0)) + 2 
                   for h, row in zip(headers, rows)]
    separator = "+" + "+".join("-" * w for w in col_widths)
    header_line = "|" + "|".join(h.ljust(w) for h, w in zip(headers, col_widths)) + "|"
    body_lines = ["|"] + [("|" + "|".join(str(r).ljust(w) if r is not None else " ".ljust(w) 
                                  for r, w in zip(row, col_widths))) + "|" 
                    for row in rows]
    return "\n".join([separator, header_line, separator] + body_lines + [separator])

def print_paginated_report(title, data_list, max_rows=10):
    if not data_list:
        print(f"[{title}] No data found.")
        return
    print(f"\n[{title}]\n")
    for i, item in enumerate(data_list[:max_rows], 1):
        print(f"{i}. {item}")
    if len(data_list) > max_rows:
        print(f"... and {len(data_list) - max_rows} more items.")
