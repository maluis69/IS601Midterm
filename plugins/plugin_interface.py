class PluginInterface:
    def execute(self, *args):
        raise NotImplementedError("Each plugin must implement the 'execute' method")
