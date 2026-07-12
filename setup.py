from setuptools import find_packages, setup
from typing import List
def get_requirements_list(filepath) -> List[str]:

    requirements = []

    HYPHEN_E_DOT = "-e ."
    with open(filepath) as file:
        contents = file.readlines()
        requirements = [x.replace("\n","") for x in contents]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="house_price_prediction",
    version="0.0.1",
    author="Aila Chandra Sekhar",
    packages=find_packages(),
    install_requires=get_requirements_list("requirements.txt")
)