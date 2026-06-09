# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: CraftFlow
def validate_entry(entry):
    if not entry.get('name'):
        raise ValueError("Entry name is required")
    if not isinstance(entry.get('id'), str) or len(entry['id']) < 3:
        raise ValueError("Entry id must be a string of at least 3 characters")
    if 'notes' in entry and (not isinstance(entry['notes'], str) or len(entry['notes']) > 500):
        raise ValueError("Notes must be a string under 500 characters")
    if 'cost' in entry and (not isinstance(entry['cost'], (int, float)) or entry['cost'] < 0):
        raise ValueError("Cost must be a non-negative number")
    return True

def validate_material(material):
    if not material.get('name'):
        raise ValueError("Material name is required")
    if 'quantity' in material and (not isinstance(material['quantity'], (int, float)) or material['quantity'] <= 0):
        raise ValueError("Quantity must be a positive number")
    return True

def validate_milestone(milestone):
    if not milestone.get('title'):
        raise ValueError("Milestone title is required")
    if 'status' in milestone and milestone['status'] not in ['planned', 'in_progress', 'completed']:
        raise ValueError("Status must be one of: planned, in_progress, completed")
    return True

def validate_inspiration(inspiration):
    if not inspiration.get('source'):
        raise ValueError("Inspiration source is required")
    if 'text' in inspiration and (not isinstance(inspiration['text'], str) or len(inspiration['text']) > 300):
        raise ValueError("Inspiration text must be under 300 characters")
    return True
