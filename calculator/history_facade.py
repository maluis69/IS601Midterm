"""
This module provides a facade interface for managing calculation history.
"""

from calculator.history import HistoryManager

class HistoryFacade:
    """
    A facade class to simplify interactions with calculation history.
    """

    def __init__(self):
        """
        Initializes the HistoryFacade with an instance of HistoryManager.
        """
        self.history_manager = HistoryManager()

    def add_operation(self, operation, operand1, operand2, result):
        """
        Adds an operation entry to the history.
        
        Args:
            operation (str): The operation performed.
            operand1 (float): The first operand.
            operand2 (float): The second operand.
            result (float): The result of the operation.
        """
        self.history_manager.add_entry(operation, operand1, operand2, result)

    def get_history(self):
        """
        Retrieves the calculation history.
        
        Returns:
            pd.DataFrame: The history DataFrame containing past calculations.
        """
        return self.history_manager.load_history()

    def clear_history(self):
        """
        Clears the entire calculation history.
        """
        self.history_manager.clear_history()
