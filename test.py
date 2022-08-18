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
        mlip = MLIP()
        mlip.load_pot()
        self.assertEqual( mlip.format , "MTP",
                        "Potential format, first line is wrong" )

        self.assertEqual( mlip.version, "1.1.0",
                        "This package works with version 1.1.0" )

        self.assertGreater( mlip.species_count, 0,
                        "`species_count` should be positive" )

        self.assertGreater( mlip.min_dist, 0.4,
                        "`mind_dist` is less than 0.4 Angstrom" )

        self.assertGreater( mlip.max_dist, 1.0,
                        "`max_dist` might be too short")

        self.assertGreater( mlip.radial_basis_size, 0,
                        "`radial_basis_size` should be positive" )

        self.assertGreater( mlip.radial_funcs_count, 0,
                        "`radial_funcs_count` should be positive" )

        self.assertGreater( mlip.radial_funcs_count, 0,
                        "`radial_funcs_count` should be positive" )

        self.assertEqual( mlip.regression_coeffs.shape[3], mlip.radial_basis_size,
                        "regression_coeffs[3] & radial_basis_size shapes")

        self.assertEqual( mlip.regression_coeffs.shape[2], mlip.radial_funcs_count,
                        "regression_coeffs[2] & radial_funcs_count shapes")

        self.assertEqual( mlip.regression_coeffs.shape[1], mlip.species_count,
                        "regression_coeffs[1] & species_count")

        self.assertEqual( mlip.regression_coeffs.shape[0], mlip.species_count,
                        "regression_coeffs[0] & species_count")

        self.assertGreater( mlip.alpha_moments_count , 0,
                        "`alpha_moments_count` should be positive" )

        self.assertGreater( mlip.alpha_index_basic_count, 0,
                        "`alpha_index_basic_count` should be positive" )

        self.assertGreater( mlip.alpha_index_times_count, 0,
                        "`alpha_index_times_count` should be positive" )

        self.assertGreater( mlip.alpha_scalar_moments, 0,
                        "`alpha_scalar_moments` should be positive" )
    #

if __name__ == "main":
    unittest.main()
#
