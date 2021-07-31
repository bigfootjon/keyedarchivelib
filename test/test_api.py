import binascii
from io import BytesIO
from unittest import TestCase

import keyedarchivelib


class TestApi(TestCase):
    def test_reversible_string(self) -> None:
        d = {"test": {"int": 2, "double": 4.0}, "string": "howdy"}
        self.assertEqual(keyedarchivelib.loads(keyedarchivelib.dumps(d)), d)

    def test_reversible_file(self) -> None:
        d = {"test": {"int": 2, "double": 4.0}, "string": "howdy"}
        file = BytesIO()
        keyedarchivelib.dump(d, file)
        self.assertEqual(keyedarchivelib.load(file), d)

    def test_keyed_archive_data(self) -> None:
        binary_data = binascii.a2b_base64(
            b"""YnBsaXN0MDDUAQIDBAUGGh1ZJGFyY2hpdmVyWCRvYmplY
            3RzVCR0b3BYJHZlcnNpb25fEA9OU0tleWVkQXJjaGl2ZXKlBw
            gREhNVJG51bGzTCQoLDA4QV05TLmtleXNaTlMub2JqZWN0c1Y
            kY2xhc3OhDYACoQ+AA4AEVHRlc3RVdmFsdWXSFBUWF1gkY2xh
            c3Nlc1okY2xhc3NuYW1loxcYGV8QE05TTXV0YWJsZURpY3Rpb
            25hcnlcTlNEaWN0aW9uYXJ5WE5TT2JqZWN00RscVGRhdGGAAR
            IAAYagCBEbJCkyREpQV19qcXN1d3l7gIaLlJ+jucbP0tfZAAA
            AAAAAAQEAAAAAAAAAHgAAAAAAAAAAAAAAAAAAAN4="""
        )
        dict_data = {"test": "value"}
        self.assertEqual(keyedarchivelib.loads(binary_data), dict_data)
