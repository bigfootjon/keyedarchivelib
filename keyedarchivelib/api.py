# pyre-strict
import plistlib
import struct
import sys
from typing import Type, Optional, BinaryIO, Dict, Any

from keyedarchivelib.compat import UID
from keyedarchivelib.util import plist_to_dict, dict_to_plist

if sys.version_info < (3, 8):
    # Versions older than 3.8 need to be hot-patched

    plistlib._BinaryPlistParser._patched_read_object = (
        plistlib._BinaryPlistParser._read_object
    )

    def _read_object(self, in_arg):
        if sys.hexversion >= 0x030605F0:
            offset = self._object_offsets[in_arg]
        else:
            offset = in_arg

        self._fp.seek(offset)
        token = self._fp.read(1)[0]
        token_l = token & 0x0F

        if token == 0x80:
            return UID(int.from_bytes(self._fp.read(1 + token_l), "big"))
        else:
            return self._patched_read_object(in_arg)

    # noinspection PyProtectedMember
    plistlib._BinaryPlistParser._read_object = _read_object

    # noinspection PyProtectedMember
    plistlib._BinaryPlistWriter._patched_write_object = (
        plistlib._BinaryPlistWriter._write_object
    )

    def _write_object(self, value):
        if isinstance(value, UID):
            ref = self._getrefnum(value)
            self._object_offsets[ref] = self._fp.tell()

            if value.data < 0:
                raise ValueError("UIDs must be positive")
            elif value.data < 1 << 8:
                self._fp.write(struct.pack(">BB", 0x80, value))
            elif value.data < 1 << 16:
                self._fp.write(struct.pack(">BH", 0x81, value))
            elif value.data < 1 << 32:
                self._fp.write(struct.pack(">BL", 0x83, value))
            elif value.data < 1 << 64:
                self._fp.write(struct.pack(">BQ", 0x87, value))
            else:
                raise OverflowError(value)
        else:
            self._patched_write_object(value)

    # noinspection PyProtectedMember
    plistlib._BinaryPlistWriter._write_object = _write_object


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
