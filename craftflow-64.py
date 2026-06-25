# === Stage 64: Add validation for relationship references ===
# Project: CraftFlow
from typing import Optional, List
import re

def validate_reference(ref_type: str, ref_value: str) -> bool:
    if not ref_value.strip():
        return False
    
    pattern_map = {
        "project_id": r"^\d{4}$",
        "user_id": r"^[a-zA-Z0-9_-]{3,20}$",
        "material_sku": r"^[A-Z]{2}-\d+$",
        "milestone_date": r"^\d{4}-\d{2}-\d{2}$",
    }
    
    if ref_type not in pattern_map:
        return True
    
    regex = re.compile(pattern_map[ref_type])
    return bool(regex.match(ref_value))

def validate_relationships(data: dict) -> List[str]:
    errors = []
    project_id = data.get("project_id")
    
    if "materials" in data and isinstance(data["materials"], list):
        for item in data["materials"]:
            sku = item.get("sku", "")
            if not validate_reference("material_sku", sku):
                errors.append(f"Invalid material SKU: {sku}")
    
    if "milestones" in data and isinstance(data["milestones"], list):
        for milestone in data["milestones"]:
            date_str = milestone.get("date", "")
            if not validate_reference("milestone_date", date_str):
                errors.append(f"Invalid milestone date: {date_str}")
            
            user_id = milestone.get("assigned_to")
            if user_id and not validate_reference("user_id", str(user_id)):
                errors.append(f"Invalid user ID reference: {user_id}")
    
    return errors
