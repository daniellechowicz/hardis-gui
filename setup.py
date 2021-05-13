from setuptools import find_packages
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="HARDIS",
    version="1.0.0",
    description="Automatic cutting force analysis",
    author="Daniel Lechowicz",
    author_mail="d.lechowicz@wood-kplus.at",
    url="https://github.com/daniellechowicz",
    packages=find_packages(),
    install_requires=required,
)