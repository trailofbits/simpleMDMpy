from pathlib import Path
from setuptools import setup  # type: ignore

with open(Path(__file__).absolute().parent / "requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    install_requires=requirements
)
