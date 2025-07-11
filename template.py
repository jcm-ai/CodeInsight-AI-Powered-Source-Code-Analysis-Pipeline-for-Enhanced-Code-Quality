import os
from pathlib import Path
import logging

# Configure logging for better visibility
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] - %(levelname)s - %(message)s')

# Define the list of files and directories for your project
project_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/main.py", # Added a common main file
    ".env",
    "setup.py",
    "app.py",
    "requirements.txt",
    "research/trials.ipynb",
    "config/config.yaml", # Example for a configuration file
    "data/.gitkeep" # Placeholder for data directory, .gitkeep ensures it's tracked
]

def setup_project_structure(files_to_create):
    """
    Sets up the project directory structure and creates specified empty files.

    Args:
        files_to_create (list): A list of file paths (strings) to create.
    """
    logging.info("Starting project structure setup...")
    for file_path_str in files_to_create:
        path = Path(file_path_str) # Convert string to Path object

        # Create parent directories if they don't exist
        if path.parent: # Check if there's a parent directory
            os.makedirs(path.parent, exist_ok=True)
            if path.parent.is_dir():
                logging.info(f"Ensured directory exists: {path.parent}")

        # Create the file if it doesn't exist or is empty
        if not path.exists() or path.stat().st_size == 0:
            try:
                with open(path, "w") as f:
                    pass  # Create an empty file
                logging.info(f"Created empty file: {path}")
            except IOError as e:
                logging.error(f"Error creating file {path}: {e}")
        else:
            logging.info(f"File already exists and is not empty: {path}")
    logging.info("Project structure setup complete.")

if __name__ == "__main__":
    setup_project_structure(project_files)
    
# This script sets up a basic project structure with specified files and directories.
# It ensures that directories are created and files are initialized as empty if they do not exist.