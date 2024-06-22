from setuptools import *

NAME = "RibbonEngine"
VERSION = "0.0.1"

setup(
    author="Warm",
    name = NAME,
    version=VERSION,
    packages=find_packages("./src"),
    requires=[
        "pysdl2"
    ],
    description="A game engine makes by SDL2"
)