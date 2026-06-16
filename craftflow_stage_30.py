# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: CraftFlow
def parse_date(text: str) -> datetime.date | None:
    """Parse date from string using multiple formats with clear error messages."""
    if not text.strip():
        return None
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%Y.%m.%d", "%B %d, %Y"):
        try:
            return datetime.strptime(text.strip(), fmt)
        except ValueError:
            continue
    raise ValueError(f"Unrecognized date format for '{text}'")

def parse_cost(text: str | None) -> float | None:
    """Parse cost string handling currency symbols and text descriptions."""
    if not text or isinstance(text, (int, float)):
        return text if isinstance(text, (int, float)) else 0.0
    clean = re.sub(r"[^\d.,-]", "", str(text).strip())
    if not clean:
        return None
    try:
        return round(float(clean.replace(",", ".")), 2)
    except ValueError as e:
        raise ValueError(f"Invalid cost format '{text}': {e}")

def parse_material(text: str | None) -> dict[str, any] | None:
    """Parse material entry expecting 'Name (Qty x Unit)' or similar."""
    if not text:
        return None
    parts = re.split(r"\s*\(\d+\s*x\s*", text.strip())
    name = parts[0].strip() if len(parts) > 1 else text.strip()
    qty_unit_match = re.search(r"\((\d+)\s+x\s*([^\)]+)\)", text, re.IGNORECASE)
    return {
        "name": name,
        "quantity": int(qty_unit_match.group(1)) if qty_unit_match else None,
        "unit": qty_unit_match.group(2).strip() if qty_unit_match else None
    }
