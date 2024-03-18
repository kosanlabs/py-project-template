# Py-project-template

Template for start new python project

# Installation

You can install the package using python interactive package (PIP)
```bash
pip install -e .
```
for develop install
```bash
pip install -e ".[dev]"
```

## Structure

Structure directory template 

```
.
├── dev-requirements.txt
├── README.md
├── requirements.txt
├── setup.py
├── src
│   ├── __init__.py
│   └── welcome.py
├── structure.txt
└── tests
    └── test_welcome.py
```

## Setting hooks

Setting hooks for better development using pre-commit by

```bash
pre-commit install
```

## Publish on pypi

> [!IMPORTANT]
Before publish, edit ``__version__`` on [``src/__init__.py``](src/__init__.py) to matching the new version.

## CI/CD

This template using Github Actions to automatically run test, and check code quality when PR is done on main.

On any pull request without publish, we use ``pre-commit`` and ``Github Action`` for code quality and tests.
