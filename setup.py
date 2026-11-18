# creating Machine learning application as a package.
from setuptools import find_packages, setup
from typing import list

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)-> list[str]:
    '''This function will return the list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements] #while reading each line it contains \n to remove it define function
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements
        
setup(
    name="MLProject",
    version="0.0.1",
    author="Nitish",
    author_email="nitishpatil1416@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)