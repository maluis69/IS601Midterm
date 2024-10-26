"""
This module manages the history of calculations using Pandas.
"""

from datetime import datetime
import pandas as pd
import os

class HistoryManager:
    """
    Manages calculation history, saving and loading from a CSV file.
    """

    def __init__(self, file_path="calculation_history.csv"):
        """
        Initializes the HistoryManager with an optional file path.
        
        Args:
            file_path (str): Path to the CSV file for storing history.
        """
        self.file_path = file_path
        self.columns = ["timestamp", "operation", "operand1", "operand2", "result"]
        try:
            self.history = pd.read_csv(self.file_path)
        except FileNotFoundError:
            self.history = pd.DataFrame(columns=self.columns)

    def add_entry(self, operation, operand1, operand2, result):
        """
        Adds an entry to the history.

        Args:
            operation (str): The operation performed (e.g., 'add', 'mul').
            operand1 (float): The first operand.
            operand2 (float): The second operand.
            result (float): The result of the operation.
        """
        new_entry = pd.DataFrame([{
            "timestamp": datetime.now(),
            "operation": operation,
            "operand1": operand1,
            "operand2": operand2,
            "result": result
        }])

        if self.history.empty:
            self.history = new_entry
        else:
            self.history = pd.concat([self.history, new_entry], ignore_index=True)

        self.history.to_csv(self.file_path, index=False)

    def load_history(self):
        """
        Loads and returns the current calculation history.

        Returns:
            pd.DataFrame: The history DataFrame containing past calculations.
        """
        return self.history

    def clear_history(self):
        """
        Clears the calculation history and updates the CSV file.
        """
        self.history = pd.DataFrame(columns=self.columns)
        self.history.to_csv(self.file_path, index=False)

    def delete_history_file(self):
        """
        Deletes the history file from the file system.
        """
        import os
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
