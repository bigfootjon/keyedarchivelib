# pyre-strict

from typing import List, Any, Dict

from keyedarchivelib.compat import UID


def plist_to_dict(plist: Dict[Any, Any]) -> Dict[Any, Any]:  # pyre-ignore
    result = {}
    objects = plist["$objects"]
    keys = objects[1]["NS.keys"]
    values = objects[1]["NS.objects"]
    assert len(keys) == len(values)
    for i in range(len(keys)):
        result[objects[keys[i]]] = objects[values[i]]
    return result


def dict_to_plist(d: Dict[Any, Any]) -> Dict[Any, Any]:  # pyre-ignore
    key_indexes = []
    value_indexes = []
    values: List[Any] = []  # pyre-ignore
    for key, _ in d.items():
        if key in values:
            ki = values.index(key) + 2
        else:
            values.append(key)
            ki = len(values) + 1
        key_indexes.append(UID(ki))

    for _, value in d.items():
        if value in values:
            vi = values.index(value) + 2
        else:
            values.append(value)
            vi = len(values) + 1
        value_indexes.append(UID(vi))
    return {
        "$archiver": "NSKeyedArchiver",
        "$objects": [
            "$null",
            {
                "NS.keys": [*key_indexes],
                "NS.objects": [*value_indexes],
                "$class": UID(len(values) + 2),
            },
            *values,
            {
                "$classes": ["NSMutableDictionary", "NSDictionary", "NSObject"],
                "$classname": "NSMutableDictionary",
            },
        ],
        "$top": {"data": UID(1)},
        "$version": 100000,
    }
