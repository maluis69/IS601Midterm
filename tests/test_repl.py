from unittest.mock import patch
from calculator.repl import repl

def dynamic_input(prompt):
    """
    A helper function to provide mock inputs based on the prompt from the REPL.
    This will dynamically match the REPL's prompts and return corresponding inputs.
    """
    print(f"DEBUG: Prompt received: {prompt}")  # To confirm what the REPL is asking for
    if "Enter command" in prompt:
        return "invalid"  # First provide an invalid command to trigger "Unknown command"
    return "quit"  # Default to "quit" for other prompts to exit the REPL

def test_invalid_command():
    """
    Test that an invalid command is handled correctly by the REPL.
    """
    with patch("builtins.input", side_effect=dynamic_input):
        with patch("builtins.print") as mock_print:
            repl()
            # Confirm that "Unknown command" was printed at least once
            mock_print.assert_any_call("Unknown command")
            # Confirm REPL exited
            mock_print.assert_any_call("Exiting REPL...")
                  