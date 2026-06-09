# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: CraftFlow
from dataclasses import dataclass, field
from datetime import date
from typing import Optional, List


@dataclass
class Material:
    name: str
    quantity: float
    unit: str
    cost: float
    supplier: Optional[str] = None


@dataclass
class Milestone:
    title: str
    target_date: date
    completed: bool = False
    notes: str = ""


@dataclass
class InspirationNote:
    source: str
    url: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    comment: str = ""


@dataclass
class ProjectRecord:
    name: str
    start_date: date
    materials: List[Material] = field(default_factory=list)
    milestones: List[Milestone] = field(default_factory=list)
    inspiration_notes: List[InspirationNote] = field(default_factory=list)
    total_budget: float = 0.0
