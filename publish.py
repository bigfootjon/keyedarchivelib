#!/usr/bin/env python3


import os

import keyedarchivelib

if os.popen("git tag -l " + keyedarchivelib.VERSION).read() == "":
    os.system(
        "git tag -a "
        + keyedarchivelib.VERSION
        + ' -m "Version '
        + keyedarchivelib.VERSION
        + '"'
    )
    os.system("git push --tags")
    os.system("python3 -m build")
    os.system("python3 -m twine upload dist/*")
else:
    print("There is already a tag for version " + keyedarchivelib.VERSION)
    print("Assuming that it exists on PyPi as well, quiting")
