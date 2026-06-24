# === Stage 61: Add performance timing for core list and search operations ===
# Project: CraftFlow
import time
from functools import wraps
from typing import Callable, Any

def timed_operation(name: str):
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = (time.perf_counter() - start) * 1000
            print(f"[{name}] {func.__qualname__}: {elapsed:.2f}ms")
            return result
        return wrapper
    return decorator

@timed_operation("Core Operations")
def search_materials(query: str, materials_list: list[dict]) -> list[dict]:
    query_lower = query.lower()
    matches = []
    for item in materials_list:
        if any(query_lower in str(v).lower() for v in item.values()):
            matches.append(item)
    return matches

@timed_operation("Core Operations")
def get_project_milestones(project_id: int, milestones_dict: dict[int, list[dict]]) -> list[dict]:
    return milestones_dict.get(project_id, [])
