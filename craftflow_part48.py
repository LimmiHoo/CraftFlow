# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: CraftFlow
import unittest
from craftflow.helpers import validate_material, calculate_total_cost, normalize_note

class TestHelpers(unittest.TestCase):
    def test_validate_material_valid(self):
        self.assertTrue(validate_material("wood", 10.5))
    
    def test_validate_material_invalid_type(self):
        with self.assertRaises(ValueError):
            validate_material(123, 10)
    
    def test_calculate_total_cost_empty_list(self):
        self.assertEqual(calculate_total_cost([]), 0)
    
    def test_normalize_note_case_insensitive(self):
        note = "Crafting a wooden chair!"
        normalized = normalize_note(note)
        self.assertEqual(normalized, "crafting a wooden chair!")

if __name__ == '__main__':
    unittest.main()
