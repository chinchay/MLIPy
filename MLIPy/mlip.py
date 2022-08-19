import numpy as np
from . import library as lib

class MLIP():
    def __init__(self) -> None:
        
        pass

    def load_pot(self, filename="work/pot.mtp"):
        lines = lib.get_lines_file(filename)
        self.format = lib.get_format(lines)
        self.version = lib.get_version(lines)
        self.species_count = lib.get_species_count(lines)
        self.min_dist = lib.get_min_dist(lines)
        self.max_dist = lib.get_max_dist(lines)
        self.radial_basis_size = lib.get_radial_basis_size(lines)
        self.radial_funcs_count = lib.get_radial_funcs_count(lines)
        self.regression_coeffs, iline = lib.get_regression_coeffs(
                                    lines, 
                                    self.species_count,
                                    self.radial_funcs_count,
                                    self.radial_basis_size
                                    )
        self.alpha_moments_count = lib.get_alpha_moments_count(lines, iline)
        self.alpha_index_basic_count = lib.get_alpha_index_basic_count(lines, iline)
        self.alpha_index_times_count = lib.get_alpha_index_times_count(lines, iline)
        self.alpha_scalar_moments = lib.get_alpha_scalar_moments(lines, iline)
        self.alpha_index_basic = lib.get_alpha_index_basic(lines, iline)
        self.alpha_index_times = lib.get_alpha_index_times(lines, iline)
        self.alpha_moment_mapping = lib.get_alpha_moment_mapping(lines, iline)
        self.species_coeffs = lib.get_species_coeffs(lines, iline)
        self.moment_coeffs = lib.get_moment_coeffs(lines, iline)
