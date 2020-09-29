import sys
import os
from pathlib import Path

levels_up = 1


def setup_imports(levels_up=1):
    current_filepath = os.path.abspath(__file__)
    parent_directory = Path(current_filepath).parents[levels_up]

    if str(parent_directory) not in sys.path:
        sys.path.insert(0, str(parent_directory))