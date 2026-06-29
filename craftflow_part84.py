# === Stage 84: Add final cleanup for unused helpers and duplicate code ===
# Project: CraftFlow
def _cleanup_unused_helpers():
    """Remove duplicate logic and consolidate utility functions."""
    # Consolidate string formatting into a single helper
    def format_currency(value):
        return f"${value:,.2f}"
    
    # Remove any global variables that were used only in deleted helpers
    if 'GLOBAL_STATS' in globals():
        del GLOBAL_STATS
    
    # Ensure no circular imports or unused module references remain
    import sys
    modules_to_remove = [mod for mod in list(sys.modules.keys()) if mod.startswith('craftflow_')]
    for mod in modules_to_remove:
        del sys.modules[mod]

_cleanup_unused_helpers()
