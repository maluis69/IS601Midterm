from calculator.history import HistoryManager
import os

def test_add_entry():
    # Use a temporary file for testing
    temp_file = "test_history.csv"
    history = HistoryManager(temp_file)
    history.clear_history()  # Clear any existing data

    history.add_entry("add", 1, 2, 3)
    assert len(history.load_history()) == 1

    # Clean up the temporary test file
    os.remove(temp_file)
