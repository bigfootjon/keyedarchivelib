# keyedarchivelib

Basic Python (>=3.8) library to generate and parse NSKeyedArchive files.

## Installation

Install with pip:

`pip3 install keyedarchivelib`

## Usage

The `keyedarchivelib` module has the same interface as the `plistlib` standard library module:

`load`, `loads`, `dump`, and `dumps` have the same function signatures as
[plistlib](https://docs.python.org/3/library/plistlib.html) minus the `fmt` option, which is not available since it's
always binary.

The `keyedarchivelib` module includes type hints.

For convenience, examples are provided below:

### Reading (`load` & `loads`)

```python
from keyedarchivelib import load

with open("example.plist", 'rb') as fp:
    pl = load(fp)
print(pl["test"])
```

### Writing (`dump` & `dumps`)

```python
from keyedarchivelib import dump, dumps

example_dict = {
    "test": 1
}
with open("example.plist", 'wb') as fp:
    dump(example_dict, fp)

# ~~~ OR ~~~

print(dumps(example_dict))
```

## Note on compatibility

For versions below 3.8, `plistlib` doesn't support all the plist features used by NSKeyedArchiver. A compatibility
hot-patching layer is used to support these lesser versions of Python. This library has not endured thorough testing
beyond the latest versions of Python 3.7-10. Please open issues for any observed problems!
