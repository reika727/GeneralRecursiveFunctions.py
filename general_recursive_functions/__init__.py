from .primitive_recursive_functions import *
from functools import cache

def mu(f):
    @cache
    def g(*args):
        i = 0
        while f(i, *args) != 0:
            i += 1
        return i
    return g
