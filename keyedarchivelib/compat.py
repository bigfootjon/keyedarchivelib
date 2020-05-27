# pyre-strict

from typing import Type, Tuple, Any

try:
    # python 3.8 and above
    from plistlib import UID
except ImportError:
    # python 3.7 and below
    class UID:
        def __init__(self, data: int) -> None:
            # pyre-ignore
            if not isinstance(data, int):
                raise TypeError("data must be an int")
            if data >= 1 << 64:
                raise ValueError("UIDs cannot be >= 2**64")
            if data < 0:
                raise ValueError("UIDs must be positive")
            self.data = data

        def __index__(self) -> int:
            return self.data

        def __repr__(self) -> str:
            return "%s(%s)" % (self.__class__.__name__, repr(self.data))

        def __reduce__(self) -> Tuple[Type["UID"], Tuple[int]]:
            return self.__class__, (self.data,)

        def __eq__(self, other: Any) -> bool:  # pyre-ignore[2]
            if not isinstance(other, UID):
                return NotImplemented
            return self.data == other.data

        def __hash__(self) -> int:
            return hash(self.data)
