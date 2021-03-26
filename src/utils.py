from typing import Tuple
from typing import Optional
from typing import Any

import yaml


def load_yaml(file_path: str) -> Tuple[Optional[Any], Optional[str]]:
    yaml_file, error = None, None
    try:
        with open(file_path, "r") as file:
            yaml_file = yaml.safe_load(file)
    except Exception as e:
        error = "Error loading the yaml template file"

        pass
    return yaml_file


def write_yaml(file_path: str):
    pass
