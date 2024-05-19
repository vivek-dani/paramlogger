from pathlib import Path
from setuptools import setup, find_packages

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
CLASSIFIERS = [
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
]
REQUIRES = []

# TODO pin down versions of libraries
TEST_REQUIRES = ["pytest"]
DEV_REQUIRES = ["twine", "wheel"]

setup(
    name="paramlogger",
    version="0.0.1",
    author="Vivek Dani",
    description="This library helps logging the inputs and outputs of a method just by adding a decorator on that method.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/vivek-dani/paramlogger",
    classifiers=CLASSIFIERS,
    install_requires=REQUIRES,
    python_requires=">=3.8",
    packages=find_packages(exclude=["tests*", "scripts*"]),
    extras_require={"test": TEST_REQUIRES, "dev": DEV_REQUIRES},
    package_data={"": ["*/*requirements.txt"]},
)
