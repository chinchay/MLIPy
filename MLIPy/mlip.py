import numpy as np
from . import library as lib

class MLIP():
    def __init__(self) -> None:
        
        pass

    def load_pot(self, filename="../work.pot.mtp"):
        lines = lib.get_lines_file(filename)
        self.format = lib.get_format(lines)
        self.version = lib.get_version(lines)
    

