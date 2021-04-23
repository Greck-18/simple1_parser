from setuptools import setup, find_packages
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def get_version():
    path = os.path.join(BASE_DIR, "VERSION")
    with open(path, "r") as version_file:
        return version_file.read().strip()


def get_license():
    return os.path.join(BASE_DIR, "LICENSE")


def get_description():
    path = os.path.join(BASE_DIR, "README.md")
    with open(path, "r") as readme_file:
        return readme_file.read().strip()


def get_requires():
    path = os.path.join(BASE_DIR, "requirements.txt")
    with open(path, "r") as req_file:
        package = [pack.strip() for pack in req_file.read().strip().split("\n")]

    return package


VERSION = get_version()

ARGS = {
    "name": "prs",
    "version": VERSION,
    "author": "Даня",
    "author_email": "greck1111@mail.ru",
    "url": "",
    "packages": find_packages("src", exclude=["*test*"]),
    "package_dir": {"": "src"},
    "include_package_data": True,
    "license": get_license(),
    "description": "News parser",
    "long_description": get_description(),
    "long_description_content_type": "text/markdown",
    "install_requires": get_requires(),
    "python_requires": ">=3.8",
    "zip_safe": False,
    "classifiers": [
        "Development Status :: 3 - Alpha"
        if "dev" in VERSION
        else "Development Status :: 4 - Beta"
        if "rc" in VERSION
        else "Development Status :: 5 - Production/Stable"
    ],
}


setup(**ARGS)
