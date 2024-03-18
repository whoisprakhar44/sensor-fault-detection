from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e.'
REQUIREMENT_FILE_NAME = 'requirements.txt'

def get_requirements() -> List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list

setup(
    name="sensor",
    version="0.0.1",
    author="Prakhar",
    author_email="prakharshukla2505@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)