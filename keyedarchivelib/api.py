import plistlib
from typing import Any, BinaryIO, Dict, Type

from keyedarchivelib.util import dict_to_plist, plist_to_dict


def load(  # pyre-ignore
    fp: BinaryIO,
    dict_type: Type[Dict[Any, Any]] = dict,  # pyre-ignore
) -> Dict[Any, Any]:
    return plist_to_dict(
        plistlib.load(fp, fmt=plistlib.FMT_BINARY, dict_type=dict_type)
    )


def loads(  # pyre-ignore
    value: bytes,
    dict_type: Type[Dict[Any, Any]] = dict,  # pyre-ignore
) -> Dict[Any, Any]:
    return plist_to_dict(
        plistlib.loads(value, fmt=plistlib.FMT_BINARY, dict_type=dict_type)
    )


def dump(
    value: Dict[Any, Any],  # pyre-ignore
    fp: BinaryIO,
    sort_keys: bool = True,
    skipkeys: bool = False,
) -> None:
    plistlib.dump(
        dict_to_plist(value),
        fp,
        fmt=plistlib.FMT_BINARY,
        sort_keys=sort_keys,
        skipkeys=skipkeys,
    )


def dumps(
    value: Dict[Any, Any],  # pyre-ignore
    skipkeys: bool = False,
    sort_keys: bool = True,
) -> bytes:
    return plistlib.dumps(
        dict_to_plist(value),
        fmt=plistlib.FMT_BINARY,
        skipkeys=sort_keys,
        sort_keys=skipkeys,
    )
