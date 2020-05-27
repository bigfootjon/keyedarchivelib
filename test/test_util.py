# pyre-strict

from unittest import TestCase

from keyedarchivelib.compat import UID
from keyedarchivelib.util import dict_to_plist, plist_to_dict


class TestBoth(TestCase):
    def test_dict_to_plist_to_dict(self) -> None:
        d = {"test": {"int": 2, "double": 4.0}, "string": "howdy"}
        self.assertEqual(plist_to_dict(dict_to_plist(d)), d)

    def test_plist_to_dict_to_plist(self) -> None:
        d = {
            "$archiver": "NSKeyedArchiver",
            "$objects": [
                "$null",
                {
                    "$class": UID(6),
                    "NS.keys": [UID(2), UID(3)],
                    "NS.objects": [UID(4), UID(5)],
                },
                "int",
                "float",
                1,
                3.1415,
                {
                    "$classes": ["NSMutableDictionary", "NSDictionary", "NSObject"],
                    "$classname": "NSMutableDictionary",
                },
            ],
            "$top": {"data": UID(1)},
            "$version": 100000,
        }
        self.assertEqual(dict_to_plist(plist_to_dict(d)), d)


class TestDictToPlist(TestCase):
    def test_basic(self) -> None:
        self.assertEqual(
            dict_to_plist({"int": 1, "float": 3.1415}),
            {
                "$archiver": "NSKeyedArchiver",
                "$objects": [
                    "$null",
                    {
                        "$class": UID(6),
                        "NS.keys": [UID(2), UID(3)],
                        "NS.objects": [UID(4), UID(5)],
                    },
                    "int",
                    "float",
                    1,
                    3.1415,
                    {
                        "$classes": ["NSMutableDictionary", "NSDictionary", "NSObject"],
                        "$classname": "NSMutableDictionary",
                    },
                ],
                "$top": {"data": UID(1)},
                "$version": 100000,
            },
        )

    def test_repeat(self) -> None:
        self.assertEqual(
            dict_to_plist({"int": 1, "float": 3.1415, "float2": 3.1415}),
            {
                "$archiver": "NSKeyedArchiver",
                "$objects": [
                    "$null",
                    {
                        "$class": UID(7),
                        "NS.keys": [UID(2), UID(3), UID(4)],
                        "NS.objects": [UID(5), UID(6), UID(6)],
                    },
                    "int",
                    "float",
                    "float2",
                    1,
                    3.1415,
                    {
                        "$classes": ["NSMutableDictionary", "NSDictionary", "NSObject"],
                        "$classname": "NSMutableDictionary",
                    },
                ],
                "$top": {"data": UID(1)},
                "$version": 100000,
            },
        )


class TestPlistToDict(TestCase):
    def test_basic(self) -> None:
        self.assertEqual(
            plist_to_dict(
                {
                    "$archiver": "NSKeyedArchiver",
                    "$objects": [
                        "$null",
                        {
                            "$class": UID(6),
                            "NS.keys": [UID(2), UID(3)],
                            "NS.objects": [UID(4), UID(5)],
                        },
                        "int",
                        "float",
                        1,
                        3.1415,
                        {
                            "$classes": [
                                "NSMutableDictionary",
                                "NSDictionary",
                                "NSObject",
                            ],
                            "$classname": "NSMutableDictionary",
                        },
                    ],
                    "$top": {"data": UID(1)},
                    "$version": 100000,
                }
            ),
            {"int": 1, "float": 3.1415},
        )
