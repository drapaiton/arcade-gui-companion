from typing import Optional
import logging
import yaml


def load_yaml(file_path: str) -> Optional[str]:
    """
    :param file_path: to read file
    :type file_path: str
    :return: content of the file
    :rtype: Optional[str]
    """
    try:
        with open(file_path, "r") as file:
            content = yaml.safe_load(file)
        return content
    except Exception as e:
        logging.error(e)


def write_yaml(file_path: str, content: str):
    """
    :param file_path: to read file
    :type file_path: str
    :param content: everything to replace inside
    :type content: str
    :return: None
    :rtype: None
    """
    try:
        with open(file_path, "w") as file:
            file.write(content)
    except Exception as e:
        logging.error(e)
