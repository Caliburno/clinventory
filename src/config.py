import os
import sys

# Detects if the application is running in a frozen state (e.g., packaged with PyInstaller)
if getattr(sys, "frozen", False):
    BASE_DIR = os.path.dirname(sys.executable) # Path to the executable
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # Path to the current script

# Define the path to the SQLite database file
DB_PATH = os.path.join(BASE_DIR, "clinventory.db")