from calculator.plugin_loader import load_plugins

def test_load_plugins():
    plugins = load_plugins()
    assert "square_plugin" in plugins
    assert hasattr(plugins["square_plugin"], "execute")
