"""
Global application module.
"""

# --- IMPORTS ---
from ciphermail.interface.cli import MainCLI


# --- CODE ---
def main() -> None:
    """
    Function to run the application.
    """

    # Initialize CLI context
    app = MainCLI()

    # Run the application
    try:
        app.run()
    
    # Keyboard interrupt error: exit and close DB connection
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
        app.db_manager.close()
    
    # Other exceptions: print error and close DB connection
    except Exception as e:
        print(f"\nError: {e}")
        app.db_manager.close()
