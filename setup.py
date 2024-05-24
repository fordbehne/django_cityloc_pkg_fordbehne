# put the contents of your README file into the long_description
from pathlib import Path

from setuptools import find_packages, setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.rst").read_text()

setup(long_description=long_description)
