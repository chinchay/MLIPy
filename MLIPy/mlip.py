import numpy as np
from . import load as load

class MLIP():
    def __init__(self) -> None:
        
        pass

    def load_pot(self, filename="work/pot.mtp"):
        lines                   = load.get_lines_file(filename)
        self.format             = load.get_format(lines)
        self.version            = load.get_version(lines)
        self.species_count      = load.get_species_count(lines)
        self.min_dist           = load.get_min_dist(lines)
        self.max_dist           = load.get_max_dist(lines)
        self.radial_basis_size  = load.get_radial_basis_size(lines)
        self.radial_funcs_count = load.get_radial_funcs_count(lines)
        self.regression_coeffs, iline = load.get_regression_coeffs(
                                    lines, 
                                    self.species_count,
                                    self.radial_funcs_count,
                                    self.radial_basis_size
                                    )
        self.moments_count     = load.get_alpha_moments_count(lines, iline)
        self.index_basic_count = load.get_alpha_index_basic_count(lines, iline)
        self.index_times_count = load.get_alpha_index_times_count(lines, iline)
        self.scalar_moments    = load.get_alpha_scalar_moments(lines, iline)
        self.index_basic       = load.get_alpha_index_basic(lines, iline)
        self.index_times       = load.get_alpha_index_times(lines, iline)
        self.moment_mapping    = load.get_alpha_moment_mapping(lines, iline)
        self.species_coeffs    = load.get_species_coeffs(lines, iline)
        self.moment_coeffs     = load.get_moment_coeffs(lines, iline)
