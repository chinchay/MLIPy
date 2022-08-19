import numpy as np

def get_lines_file(filename):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    return lines
    # TODO: Add exception handling or debug.ERROR
#

def get_format(lines):
    return lines[0].strip()
#

def get_parameter(lines, line_number):
    return lines[line_number].split("=")[1].strip()
#

def get_version(lines):
    return get_parameter(lines, 1)
#

def get_species_count(lines):
    return int(get_parameter(lines, 4))

def get_min_dist(lines):
    return float(get_parameter(lines, 7))

def get_max_dist(lines):
    return float(get_parameter(lines, 8))

def get_radial_basis_size(lines):
    return int(get_parameter(lines, 9))

def get_radial_funcs_count(lines):
    return int(get_parameter(lines, 10))

def get_regression_coeffs(
                        lines,
                        species_count,
                        radial_funcs_count,
                        radial_basis_size
                        ):
    regression_coeffs = np.zeros( ( species_count,
                                    species_count,
                                    radial_funcs_count,
                                    radial_basis_size
                                ),
                                dtype=float)
    #
    iline = 12
    for s1 in range(species_count):
        for s2 in range(species_count):
            iline += 1
            for i in range(radial_funcs_count):
                list_t = lines[iline].strip( '\t\{\}\n' ).split(',')
                iline += 1
                for j in range(radial_basis_size):
                    regression_coeffs[s1, s2, i, j] = float( list_t[j] )
    #
    return regression_coeffs, iline
#

def get_alpha_moments_count(lines, iline):
    return int(get_parameter(lines, iline))
#

def get_alpha_index_basic_count(lines, iline):
    return int(get_parameter(lines, iline + 1))

def get_alpha_index_times_count(lines, iline):
    return int(get_parameter(lines, iline + 3))

def get_alpha_scalar_moments(lines, iline):
    return int(get_parameter(lines, iline + 5))

def get_vector(lines, iline):
    string = get_parameter(lines, iline).replace("{", "[").replace("}", "]")
    return np.asarray( eval( string ) )

def get_alpha_index_basic(lines, iline):
    return get_vector(lines, iline + 2)

def get_alpha_index_times(lines, iline):
    return get_vector(lines, iline + 4)

def get_alpha_moment_mapping(lines, iline):
    return get_vector(lines, iline + 6)

def get_species_coeffs(lines, iline):
    return get_vector(lines, iline + 7)

def get_moment_coeffs(lines, iline):
    return get_vector(lines, iline + 8)


