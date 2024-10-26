import importlib
import os

def load_plugins():
    plugins = {}
    plugin_dir = "plugins"
    for file in os.listdir(plugin_dir):
        if file.endswith("_plugin.py"):
            module_name = file[:-3]
            module = importlib.import_module(f"plugins.{module_name}")
            class_name = ''.join([word.capitalize() for word in module_name.split('_')])
            plugins[module_name] = getattr(module, class_name)()
    return plugins
