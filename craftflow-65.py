# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: CraftFlow
from typing import Dict, List, Optional
import re

def merge_imports(existing: List[str], new_code: str) -> tuple[List[str], bool]:
    existing_set = set(existing)
    found_duplicates = False
    merged_lines = []
    for line in new_code.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            merged_lines.append(line)
            continue
        import_match = re.match(r'^import\s+([\w,.\s]+)$', stripped)
        from_match = re.match(r'^from\s+(\w+)\s+import\s+(.+)$', stripped)
        if not import_match and not from_match:
            merged_lines.append(line)
            continue
        imports_to_add = []
        if import_match:
            modules_str = import_match.group(1).replace(', ', ',')
            for part in modules_str.split(','):
                module_name = part.strip().split('.')[0]
                if module_name not in existing_set:
                    imports_to_add.append(f'import {module_name}')
        elif from_match:
            module_name = from_match.group(1)
            items_str = from_match.group(2).replace(', ', ',')
            for item in items_str.split(','):
                item_parts = item.strip().split()
                if len(item_parts) == 2:
                    alias, name = item_parts[0], item_parts[1]
                    target_name = name if not alias else f'{name} as {alias}'
                    key = module_name + '.' + target_name
                    if key not in existing_set and (module_name not in existing_set or 
                        (from_match.group(2).replace(', ', '').split() and item_parts[1] == 'as' and len(item_parts) > 3)):
                         imports_to_add.append(f'from {module_name} import {target_name}')
        elif from_match:
            module_name = from_match.group(1)
            items_str = from_match.group(2).replace(', ', ',')
            for item in items_str.split(','):
                item_parts = item.strip().split()
                if len(item_parts) == 2:
                    alias, name = item_parts[0], item_parts[1]
                    target_name = name if not alias else f'{name} as {alias}'
                    key = module_name + '.' + target_name
                    if key not in existing_set and (module_name not in existing_set or 
                        (from_match.group(2).replace(', ', '').split() and item_parts[1] == 'as' and len(item_parts) > 3)):
                         imports_to_add.append(f'from {module_name} import {target_name}')
        if imports_to_add:
            merged_lines.extend(imports_to_add)
            existing_set.update([l.strip().replace('import ', '').split()[0] for l in imports_to_add])
            found_duplicates = True
    return merged_lines, found_duplicates
