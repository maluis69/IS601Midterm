from plugins.plugin_interface import PluginInterface

class SquarePlugin(PluginInterface):
    def execute(self, a):
        """
        Returns the square of the given number.
        
        Args:
            a (float): The number to square.
        
        Returns:
            float: The square of the number.
        """
        return a ** 2