# === Stage 56: Add compact error classes for domain failures ===
# Project: CraftFlow
class CraftError(Exception): pass
class MaterialNotFoundError(CraftError): pass
class MilestoneMissedError(CraftError): pass
class BudgetOverrunError(CraftError): pass
class InspirationMissingError(CraftError): pass
class ProjectClosedEarlyError(CraftError): pass
class ResourceConflictError(CraftError): pass
