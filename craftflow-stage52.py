# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: CraftFlow
def format_currency(amount: float, currency: str = "USD") -> str:
    """Format a monetary amount with locale-aware symbols and two decimal places."""
    if currency == "EUR":
        symbol = "€"
    elif currency == "GBP":
        symbol = "£"
    else:
        symbol = "$"
    return f"{symbol}{amount:.2f}"

def parse_date(date_str: str, format_type: str = "iso") -> datetime.date | None:
    """Parse a date string into a standard date object based on the specified format type."""
    formats_map = {
        "iso": "%Y-%m-%d",
        "us": "%m/%d/%Y",
        "eu": "%d.%m.%Y"
    }
    fmt = formats_map.get(format_type, "%Y-%m-%d")
    try:
        return datetime.datetime.strptime(date_str.strip(), fmt).date()
    except ValueError:
        return None

def validate_material_entry(entry: dict) -> tuple[bool, str]:
    """Validate a material entry dictionary and return success status with error message."""
    required_keys = {"name", "quantity", "cost"}
    if not all(key in entry for key in required_keys):
        missing = required_keys - set(entry.keys())
        return False, f"Missing keys: {', '.join(missing)}"
    try:
        float(entry["quantity"])
        float(entry["cost"])
    except (TypeError, ValueError):
        return False, "Quantity and cost must be numeric values."
    if entry.get("name", "").strip() == "":
        return False, "Material name cannot be empty."
    return True, ""

def generate_milestone_summary(milestones: list[dict]) -> str:
    """Generate a human-readable summary string from a list of milestone dictionaries."""
    if not milestones:
        return "No milestones recorded yet."
    lines = ["Project Milestone Summary:", "=" * 30]
    for i, m in enumerate(milestones, 1):
        name = m.get("name", f"Milestone {i}")
        status = m.get("status", "pending")
        date_str = m.get("date", "")
        lines.append(f"{i}. {name} [{status}] {date_str if date_str else 'TBD'}")
    return "\n".join(lines)

def calculate_total_cost(materials: list[dict]) -> float:
    """Calculate the total cost of all provided material entries."""
    total = 0.0
    for mat in materials:
        try:
            qty = float(mat.get("quantity", 1))
            price = float(mat.get("cost", 0))
            total += qty * price
        except (TypeError, ValueError):
            continue
    return round(total, 2)

def filter_by_status(milestones: list[dict], status: str) -> list[dict]:
    """Filter a list of milestones by their current status string."""
    return [m for m in milestones if m.get("status", "").lower() == status.lower()]
