# === Stage 51: Add unit tests for search and filter behavior ===
# Project: CraftFlow
from unittest.mock import patch, MagicMock
import pytest
from craftflow.core.search_engine import SearchEngine

@pytest.fixture
def search_engine():
    return SearchEngine()

@patch('craftflow.core.search_engine._search_materials')
@patch('craftflow.core.search_engine._search_milestones')
@patch('craftflow.core.search_engine._search_costs')
@patch('craftflow.core.search_engine._search_inspiration')
def test_search_filters(search_insp, search_cost, search_mil, search_mat):
    search_mat.return_value = [{'id': 1, 'name': 'wood', 'category': 'material'}]
    search_mil.return_value = [{'id': 2, 'name': 'cut wood', 'status': 'done'}]
    search_cost.return_value = []
    search_insp.return_value = []

    engine = SearchEngine()
    
    # Test material filter by category
    results = engine.search(filter_type='material', query='wood')
    assert len(results) == 1
    
    # Test milestone filter by status
    results = engine.search(filter_type='milestone', query='done')
    assert len(results) == 1

@patch('craftflow.core.search_engine._search_materials')
def test_search_no_results(search_mat):
    search_mat.return_value = []
    
    engine = SearchEngine()
    results = engine.search(filter_type='material', query='nonexistent')
    assert results == []
