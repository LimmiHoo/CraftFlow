# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: CraftFlow
import unittest
from craftflow import Project, Material, Milestone

class TestProjectEdgeCases(unittest.TestCase):
    def setUp(self):
        self.project = Project("Test")

    def test_update_nonexistent_material_raises(self):
        with self.assertRaises(ValueError):
            self.project.update_material(999, {"name": "New", "cost": 10})

    def test_delete_nonexistent_milestone_raises(self):
        with self.assertRaises(KeyError):
            del self.project.milestones[999]

    def test_update_with_empty_dict_unchanged(self):
        mat = Material("Wood", cost=5)
        self.project.add_material(mat)
        original_cost = mat.cost
        self.project.update_material(0, {})  # Should not change anything if logic checks for changes
        self.assertEqual(mat.cost, original_cost)

    def test_delete_milestone_removes_from_dict(self):
        ms = Milestone("Finish", done=True)
        self.project.add_milestone(ms)
        del self.project.milestones[0]
        with self.assertRaises(KeyError):
            _ = self.project.milestones[0]

    def test_update_material_invalid_cost_type_raises(self):
        mat = Material("Wood", cost=5)
        self.project.add_material(mat)
        with self.assertRaises(TypeError):
            self.project.update_material(0, {"cost": "five"})
