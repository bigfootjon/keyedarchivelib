# pyre-ignore-all-errors
from distutils.core import setup

import setuptools  # type: ignore

import keyedarchivelib

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="keyedarchivelib",
    package_data={"keyedarchivelib": ["py.typed"]},
    packages=setuptools.find_packages(exclude=["test", "test.*"]),
    version=keyedarchivelib.VERSION,
    python_requires=">=3.6",
    description="Generate and parse NSKeyedArchive files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[],
    license="GNU Lesser General Public License v3 (LGPLv3)",
    author="Jonathan Janzen",
    author_email="jjjonjanzen@gmail.com",
    url="https://github.com/bigfootjon/keyedarchivelib",
    download_url="https://github.com/bigfootjon/keyedarchivelib/tarball/"
    + keyedarchivelib.VERSION,
    keywords=[],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Typing :: Typed",
    ],
)
