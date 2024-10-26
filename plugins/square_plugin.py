from plugins.plugin_interface import PluginInterface

class SquarePlugin(PluginInterface):
    def execute(self, a):
        return a ** 2
