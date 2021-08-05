import os
import subprocess
from typing import Dict

import yaml


def read_yaml(file_name: str) -> Dict:
    assert os.path.exists(file_name), f"file {file_name} does not exist"
    with open(file_name, "r") as stream:
        try:
            yaml_file = yaml.safe_load(stream)
            return yaml_file
        except yaml.YAMLError as e:
            print(e)


def run_command(cmd: list) -> None:
    return_obj = subprocess.run(cmd)
    # return_obj.check_returncode()
    # print(return_obj)
