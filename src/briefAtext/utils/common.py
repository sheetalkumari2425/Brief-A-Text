import os
from box.exceptions import BoxValueError
import yaml
from briefAtext.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


"""read yaml file and returns
        Args:path_to_yaml (str): path like input
        Raises:ValueError: if yaml file is empty
        e: empty file
        Returns:ConfigBox: ConfigBox type
"""
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        # print("inside try")
        with open(path_to_yaml) as yaml_file:
            # print("inside loop")
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            # print("read_yaml is completed")
            return ConfigBox(content)    
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        # print("different exception")
        raise e
    


"""create list of directories
    Args:path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Default to false
"""    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    # print("inside create_directories")
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")
        else:
            logger.info(f"got some error")



"""get size in KB
    Args: path (Path): path of the file
    Returns: str- size in KB
"""
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
