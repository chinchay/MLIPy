import numpy as np

def get_lines_file(filename):
    """Get each line of a file and store them in string arrays

    Args:
        filename (str): Name of the file to read

    Returns:
        list(str): List of the lines read
    """
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    return lines
    # TODO: Add exception handling or debug.ERROR

def get_format(lines):
    """Format of the potential file

    Args:
        lines (list of str): List of lines, each array as a string

    Returns:
        str: Format of the MTP file
    """
    return lines[0].strip()

def get_parameter(lines, line_number):
    """Obtain the value at the other side of `=`

    Args:
        lines (list of str): List of lines
        line_number (int): The line from which the parameter value is obtained

    Returns:
        str: value of the parameter
    """
    return lines[line_number].split("=")[1].strip()

def get_version(lines):
    """Version of the potential file

    Args:
        lines (list of str): List of lines

    Returns:
        str: version of the MTP file
    """
    return get_parameter(lines, 1)

def get_species_count(lines):
    """Get the number of species the potential was trained for

    Args:
        lines (list of str): List of lines

    Returns:
        int: number of species
    """
    return int(get_parameter(lines, 4))

def get_min_dist(lines):
    """Minimum distance the potential was trained for

    Args:
        lines (list of str): List of lines

    Returns:
        float: Minimum distance
    """
    return float(get_parameter(lines, 7))

def get_max_dist(lines):
    """Maximum distance the potential was trained for

    Args:
        lines (list of str): List of lines

    Returns:
        float: Maximum distance
    """
    return float(get_parameter(lines, 8))

def get_radial_basis_size(lines):
    """Obtain the radial_basis_size parameter value

    Args:
        lines (list of str): List of lines

    Returns:
        int: radial_basis_size parameter value
    """
    return int(get_parameter(lines, 9))

def get_radial_funcs_count(lines):
    """Obtain the radial_funcs_count parameter value

    Args:
        lines (list of str): List of lines

    Returns:
        int: radial_funcs_count parameter value
    """
    return int(get_parameter(lines, 10))

def brackets_to_array(string):
    """Convert a string with curly brackets to a numpy array
    ## Example:
    "{{1,2},{3,4}}" is converted to [ [1, 2],[3, 4] ]

    Args:
        string (str): A string with curly brackets and numbers

    Returns:
        numpy array
    """
    return np.asarray( eval( string.replace("{", "[").replace("}", "]") ) )

def get_regression_coeffs(
                        lines,
                        species_count,
                        radial_funcs_count,
                        radial_basis_size
                        ):
    """Get radial_coeffs values from the potential file

    Args:
        lines (list of str): List of lines
        species_count (int): number of species for which the potential was trained for
        radial_funcs_count (int)
        radial_basis_size (int)

    Returns:
        radial_coeffs (numpy array): radial_coeffs values
    """
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
                arr = brackets_to_array( lines[iline] )
                regression_coeffs[s1, s2, i, :] = arr
                iline += 1
    #
    return regression_coeffs, iline
#

def get_alpha_moments_count(lines, iline):
    """Get alpha_moments_count parameter value

    Args:
        lines (list of str): List of lines
        iline (int): The line from which the parameter value is obtained

    Returns:
        int: alpha_moments_count value
    """
    return int(get_parameter(lines, iline))
#

def get_alpha_index_basic_count(lines, iline):
    return int(get_parameter(lines, iline + 1))

def get_alpha_index_times_count(lines, iline):
    """Get the alpha_index_times_count parameter value

    Args:
        lines (list of str): List of lines
        iline (int): The line from which the parameter value is obtained

    Returns:
        int: alpha_index_times_count value
    """
    return int(get_parameter(lines, iline + 3))

def get_alpha_scalar_moments(lines, iline):
    """Get the alpha_scalar_moments parameter value

    Args:
        lines (list of str): List of lines
        iline (int): The line from which the parameter value is obtained

    Returns:
        int: alpha_scalar_moments value
    """
    return int(get_parameter(lines, iline + 5))

def get_array(lines, iline):
    """Obtain the string at the rigth side of `=` and convert it to a numpy array

    Args:
        lines (list of str): List of lines
        iline (int): The line from which the parameter value is obtained

    Returns:
        numpy array
    """
    return brackets_to_array( get_parameter(lines, iline) )

def get_alpha_index_basic(lines, iline):
    """Get the alpha_index_basic parameter value from the potential file

    Args:
        lines (list of str): List of lines
        iline (int): The line from which the parameter value is obtained

    Returns:
        numpy array: parameter values
    """
    return get_array(lines, iline + 2)

def get_alpha_index_times(lines, iline):
    """Get the alpha_index_times parameter value from the potential file

    Args:
        lines (list of str): List of lines
        iline (int): The line from which the parameter value is obtained

    Returns:
        numpy array: parameter values
    """
    return get_array(lines, iline + 4)

def get_alpha_moment_mapping(lines, iline):
    """Get the alpha_moment_mapping parameter values

    Args:
        lines (list of str): List of lines
        iline (int): The line from which the parameter value is obtained

    Returns:
        numpy array: parameter values
    """
    return get_array(lines, iline + 6)

def get_species_coeffs(lines, iline):
    """Get the species_coeffs parameter values from the potential file

    Args:
        lines (list of str): List of lines
        iline (int): The line from which the parameter value is obtained

    Returns:
        numpy array: parameter values
    """
    return get_array(lines, iline + 7)

def get_moment_coeffs(lines, iline):
    """Get the moment_coeffs parameter values from the potential file

    Args:
        lines (list of str): List of lines
        iline (int): The line from which the parameter value is obtained

    Returns:
        numpy array: parameter values
    """
    return get_array(lines, iline + 8)


