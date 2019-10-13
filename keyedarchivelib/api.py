# pyre-strict
import plistlib
from typing import Type, Optional, BinaryIO, Dict, Any

from keyedarchivelib.util import plist_to_dict, dict_to_plist


def load(  # pyre-ignore
    fp: BinaryIO,
    *,
    fmt: Optional[plistlib.PlistFormat] = None,
    dict_type: Type[Dict[Any, Any]] = dict  # pyre-ignore
) -> Dict[Any, Any]:
    return plist_to_dict(plistlib.load(fp, fmt=fmt, dict_type=dict_type))


def loads(  # pyre-ignore
    value: bytes,
    *,
    fmt: Optional[plistlib.PlistFormat] = None,
    dict_type: Type[Dict[Any, Any]] = dict  # pyre-ignore
) -> Dict[Any, Any]:
    return plist_to_dict(plistlib.loads(value, fmt=fmt, dict_type=dict_type))


def dump(
    value: Dict[Any, Any],  # pyre-ignore
    fp: BinaryIO,
    *,
    fmt: plistlib.PlistFormat = plistlib.FMT_XML,
    sort_keys: bool = True,
    skipkeys: bool = False
) -> None:
    plistlib.dump(
        dict_to_plist(value), fp, fmt=fmt, sort_keys=sort_keys, skipkeys=skipkeys
    )


def dumps(
    value: Dict[Any, Any],  # pyre-ignore
    *,
    fmt: plistlib.PlistFormat = plistlib.FMT_XML,
    skipkeys: bool = False,
    sort_keys: bool = True
) -> bytes:
    return plistlib.dumps(
        dict_to_plist(value), fmt=fmt, skipkeys=sort_keys, sort_keys=skipkeys
    )
