import setuptools
from setuptools import find_packages
import re

with open("./src/__init__.py", "r") as f:
    content = f.read()
    project_version = re.search(
        r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]', content
    ).group(1)

with open("README.md", "r") as f_readme:
    long_description = f_readme.read()

setuptools.setup(
    name="NAME_YOUR_PROJECT#1",
    version=project_version,
    author_email="YOUR_EMAIL@email.com",
    description="YOUR_DESCRIPTION",
    long_description=long_description,
    long_description_contet_type="text/markdown",
    url="YOUR_URL_PROJECT",
    install_requires=[
        # LIST LIBRARY REQUIRE FOR PROJECT
    ],
    packages=find_packages(exclude=("tests",)),
    extra_require={
        "dev": ["flake8", "black", "isort", "twine", "pytest", "wheel"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # python version require recommended 3.8 or 3.7
    python_requires=">=3.8"
)
