# Lattice paths 15.py

from functools import lru_cache
@lru_cache()
def lattice_paths(a,b):
    if a == 0 or b == 0: return 1
    return lattice_paths(a-1,b) + lattice_paths(a,b-1)

print(lattice_paths(20,20))