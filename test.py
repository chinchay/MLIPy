import unittest
import numpy as np
from MLIPy import MLIP
from MLIPy import library as lib

class TestMlipClass(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_initialize(self):
        mlip = MLIP()



if __name__ == "main":
    unittest.main()
#
