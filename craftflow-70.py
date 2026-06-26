# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: CraftFlow
def clear_state():
    if input("Are you sure you want to clear all data? (y/n): ") != "y":
        return False
    for key in list(CRAFT_DATA.keys()):
        del CRAFT_DATA[key]
    print("All project data cleared successfully.")
    return True
