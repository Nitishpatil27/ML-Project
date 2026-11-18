# creating Machine learning application as a package.
from setuptools import find_packages, setup


setup(
    name="MLProject",
    version="0.0.1",
    author="Nitish",
    author_email="nitishpatil1416@gmail.com",
    packages=find_packages(),
    install_requires=["pandas", "numpy", "seaborn"],
)