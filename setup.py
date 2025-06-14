from typing import TYPE_CHECKING
from setuptools import setup, find_packages  # type: ignore

if TYPE_CHECKING:
    VERSION: str = ""

with open("README.md", "r") as readme_file:
    long_description: str = readme_file.read()

with open("keyedarchivelib/version.py", "r") as version_file:
    exec(version_file.read())

setup(
    name="keyedarchivelib",
    package_data={"keyedarchivelib": ["py.typed"]},
    packages=find_packages(exclude=["test", "test.*"]),
    version=VERSION,  # noqa: F821
    python_requires=">=3.8",
    description="Generate and parse NSKeyedArchive files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[],
    license="GNU Lesser General Public License v3 (LGPLv3)",
    author="Jonathan Janzen",
    author_email="jon@jonjanzen.com",
    url="https://github.com/bigfootjon/keyedarchivelib",
    download_url="https://github.com/bigfootjon/keyedarchivelib/tarball/"
    + VERSION,  # noqa: F821
    keywords=[],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3 :: Only",
        "Typing :: Typed",
    ],
)
