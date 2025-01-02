from functools import cache

def C0(*_):
    return 0

def S(n):
    return n + 1

def P(i):
    return lambda *args: args[i - 1]

def composition(f, *gs):
    return cache(lambda *args: f(*(g(*args) for g in gs)))

def primitive_recursion(f, g):
    @cache
    def h(m, *args):
        return f(*args) if m == 0 else g(m - 1, h(m - 1, *args), *args)
    return h
