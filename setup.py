from setuptools import find_packages,setup
from typing import List

ignore = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if ignore in requirements:
            requirements.remove(ignore)
        return requirements

setup(
    name="Diamond_Price_prediction",
    version="0.0.1",
    author="Meet vasa",
    author_email="meet2work09@gmail.com",
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()

)