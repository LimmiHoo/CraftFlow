# === Stage 83: Add regression tests for the final demo workflow ===
# Project: CraftFlow
import pytest
from craftflow import Project, Material, Milestone, CostNote, InspirationNote

@pytest.fixture
def demo_project():
    p = Project(name="Demo Craft", budget=1000)
    m1 = Material(name="Wood", cost=50, quantity=2)
    m2 = Material(name="Glue", cost=5, quantity=1)
    p.add_material(m1)
    p.add_material(m2)
    ms1 = Milestone(title="Base Build", status="done")
    ms2 = Milestone(title="Painting", status="in_progress")
    p.add_milestone(ms1)
    p.add_milestone(ms2)
    c1 = CostNote(description="Initial setup", amount=50, date="2023-01-01")
    i1 = InspirationNote(source="Nature", text="Organic shapes")
    p.add_cost(c1)
    p.add_inspiration(i1)
    return p

def test_demo_workflow_regression(demo_project):
    assert demo_project.name == "Demo Craft"
    assert len(demo_project.materials) == 2
    assert demo_project.materials[0].name == "Wood"
    assert demo_project.materials[1].cost == 5
    assert len(demo_project.milestones) == 2
    assert demo_project.milestones[0].status == "done"
    assert demo_project.milestones[1].title == "Painting"
    assert len(demo_project.cost_notes) == 1
    assert demo_project.cost_notes[0].amount == 50
    assert len(demo_project.inspiration_notes) == 1
    assert demo_project.inspiration_notes[0].source == "Nature"
