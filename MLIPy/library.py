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
