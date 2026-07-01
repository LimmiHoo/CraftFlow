# === Stage 88: Add safer defaults for empty input and missing optional fields ===
# Project: CraftFlow
def safe_get(data, key, default=None):
    return data.get(key) if isinstance(data, dict) else getattr(data, key, default)

def parse_amount(value: str | None) -> float:
    try:
        clean = value.strip().replace(',', '.').lower()
        if not clean or clean in ('n/a', 'none', '-', ''):
            return 0.0
        return float(clean)
    except (ValueError, AttributeError):
        return 0.0

def parse_date(value: str | None) -> datetime.date | None:
    if not value:
        return None
    for fmt in ('%Y-%m-%d', '%d.%m.%Y', '%m/%d/%Y'):
        try:
            return datetime.datetime.strptime(value.strip(), fmt).date()
        except ValueError:
            continue
    return None

def normalize_note(text: str | None) -> str:
    if not text:
        return ''
    return ' '.join(text.replace('\n', ' ').strip().split())
