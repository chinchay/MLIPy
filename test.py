import unittest
import numpy as np
from MLIPy import MLIP
from MLIPy import library as lib

class TestMlipClass(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_initialize(self):
        mlip = MLIP()

    def test_load_pot(self):
        pot = MLIP.load_pot()
        self.assertEqual( pot.head "MTP", "Potential first line is wrong" )
        self.assertGreater( pot.species_count, 0, "`species_count` should be positive" )
        self.assertGreater( pot.min_dist, 0.4, "`mind_dist` is less than 0.4 Angstrom" )
        self.assertGreater( pot.max_dist, 1.0, "`max_dist` might be too short"  )
        self.assertGreater( pot.radial_basis_size, 0, "`radial_basis_size` should be positive" )
        self.assertGreater( pot.radial_funcs_count, 0, "`radial_funcs_count` should be positive" )
        self.assertGreater( pot.radial_funcs_count, 0, "`radial_funcs_count` should be positive" )

        self.assertGreater( pot.alpha_moments_count , 0, "`alpha_moments_count` should be positive" )
        self.assertGreater( pot.alpha_index_basic_count, 0, "`alpha_index_basic_count` should be positive" )
        self.assertGreater( pot.alpha_index_times_count, 0, "`alpha_index_times_count` should be positive" )
        self.assertGreater( pot.alpha_scalar_moments, 0, "`alpha_scalar_moments` should be positive" )
    #

if __name__ == "main":
    unittest.main()
#
