import pathlib
import unittest

from gribby import Grib2

class TestSuite(unittest.TestCase):
    """
    Test suite for GRIB2 functionality
    """

    def _resource_path(self, filename):
        p = pathlib.Path(__file__).parents[0]
        p = p / 'data' / filename
        return p


    def test_edition(self):
        """
        SCENARIO:  Open a GRB2 file.

        EXPECTED RESPONSE:  The edition specifies GRIB2.
        """
        path = self._resource_path('201804051345.15.grb2')
        gb = Grib2(path)
        self.assertEqual(gb.edition, 2)

