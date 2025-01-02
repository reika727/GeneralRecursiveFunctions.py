from general_recursive_functions import *
from functools import cache

def beta(b, f):
    @cache
    def g(*args):
        bound = b(*args)
        for i in range(bound):
            if f(i, *args) == 0:
                return i
        else:
            return bound
    return g

def for_all(b, f):
    return composition(
        is_equal_to,
        beta(b, f),
        b
    )

def for_any(b, f):
    return composition(
        logical_not,
        composition(
            is_equal_to,
            beta(b, composition(logical_not, f)),
            b
        )
    )

C1 = composition(S, C0)

C2 = composition(S, C1)

C3 = composition(S, C2)

plus2 = composition(S, S)

add = primitive_recursion(P(1), composition(S, P(2)))

double = composition(add, P(1), P(1))

multiply = primitive_recursion(C0, composition(add, P(2), P(3)))

exponentiate = composition(primitive_recursion(C1, composition(multiply, P(2), P(3))), P(2), P(1))

predecessor_of = primitive_recursion(C0, P(1))

subtract = composition(primitive_recursion(P(1), composition(predecessor_of, P(2))), P(2), P(1))

is_zero = primitive_recursion(C1, C0)

is_less_than_or_equal_to = composition(is_zero, subtract)

is_greater_than_or_equal_to = composition(is_less_than_or_equal_to, P(2), P(1))

if_then_else = primitive_recursion(P(2), P(3))

logical_and = composition(if_then_else, P(1), P(2), C0)

logical_or = composition(if_then_else, P(1), C1, P(2))

logical_not = composition(if_then_else, P(1), C0, C1)

is_equal_to = composition(logical_and, is_less_than_or_equal_to, is_greater_than_or_equal_to)

is_less_than = composition(logical_and, is_less_than_or_equal_to, composition(logical_not, is_equal_to))

is_greater_than = composition(logical_and, is_greater_than_or_equal_to, composition(logical_not, is_equal_to))

remainder_of = primitive_recursion(
    C0,
    composition(
        if_then_else,
        composition(
            is_equal_to,
            composition(S, P(2)),
            P(3)
        ),
        C0,
        composition(S, P(2))
    )
)

is_divisible_by = composition(is_zero, remainder_of)

divide = primitive_recursion(
    C0,
    composition(
        if_then_else,
        composition(
            is_equal_to,
            composition(
                S,
                composition(
                    remainder_of,
                    P(1),
                    P(3)
                )
            ),
            P(3)
        ),
        composition(S, P(2)),
        P(2)
    )
)

nth_root_of = primitive_recursion(
    C0,
    composition(
        if_then_else,
        composition(
            is_less_than_or_equal_to,
            composition(
                exponentiate,
                composition(
                    S,
                    P(2)
                ),
                P(3)
            ),
            composition(
                S,
                P(1)
            )
        ),
        composition(
            S,
            P(2)
        ),
        P(2)
    )
)

square_root_of = composition(nth_root_of, P(1), C2)

cubic_root_of = composition(nth_root_of, P(1), C3)

is_prime = composition(
    logical_and,
    composition(
        is_greater_than_or_equal_to,
        P(1),
        C2
    ),
    for_all(
        composition(composition(predecessor_of, square_root_of), P(1)),
        composition(
            logical_not,
            composition(
                is_divisible_by,
                P(2),
                composition(add, P(1), C2)
            )
        )
    )
)

count_primes = primitive_recursion(
    C0,
    composition(
        if_then_else,
        composition(is_prime, P(1)),
        composition(S, P(2)),
        P(2)
    )
)

nth_prime = beta(
    composition(
        add,
        composition(multiply, S, S),
        C2
    ),
    composition(
        logical_not,
        composition(
            logical_and,
            composition(
                is_equal_to,
                composition(count_primes, P(1)),
                P(2)
            ),
            composition(
                is_equal_to,
                composition(is_prime, P(1)),
                C1
            )
        )
    )
)

length_of = mu(
    composition(
        is_divisible_by,
        P(2),
        composition(
            nth_prime,
            P(1)
        )
    )
)

subscript = composition(
    subtract,
    mu(
        composition(
            is_divisible_by,
            P(2),
            composition(
                exponentiate,
                composition(
                    nth_prime,
                    P(3)
                ),
                P(1)
            )
        )
    ),
    C2
)

last_of = composition(
    subscript,
    P(1),
    composition(
        predecessor_of,
        length_of
    )
)

pushed = composition(
    multiply,
    P(1),
    composition(
        exponentiate,
        composition(
            nth_prime,
            composition(
                length_of,
                P(1)
            )
        ),
        composition(
            S,
            P(2)
        )
    )
)

popped = composition(
    divide,
    P(1),
    composition(
        exponentiate,
        composition(
            nth_prime,
            composition(
                predecessor_of,
                composition(
                    length_of,
                    P(1)
                )
            )
        ),
        composition(
            S,
            composition(
                last_of,
                P(1)
            )
        )
    )
)

Ack_seq = composition(
    primitive_recursion(
        composition(
            multiply,
            composition(
                exponentiate,
                C2,
                composition(
                    S,
                    P(1)
                )
            ),
            composition(
                exponentiate,
                C3,
                composition(
                    S,
                    P(2)
                )
            ),
        ),
        composition(
            if_then_else,
            composition(
                is_zero,
                composition(
                    last_of,
                    composition(
                        popped,
                        P(2)
                    )
                )
            ),
            composition(
                pushed,
                composition(
                    popped,
                    composition(
                        popped,
                        P(2)
                    )
                ),
                composition(
                    S,
                    composition(
                        last_of,
                        P(2)
                    )
                )
            ),
            composition(
                if_then_else,
                composition(
                    logical_and,
                    composition(
                        is_zero,
                        composition(
                            last_of,
                            P(2)
                        )
                    ),
                    composition(
                        logical_not,
                        composition(
                            is_zero,
                            composition(
                                last_of,
                                composition(
                                    popped,
                                    P(2)
                                )
                            )
                        )
                    )
                ),
                composition(
                    pushed,
                    composition(
                        pushed,
                        composition(
                            popped,
                            composition(
                                popped,
                                P(2)
                            )
                        ),
                        composition(
                            predecessor_of,
                            composition(
                                last_of,
                                composition(
                                    popped,
                                    P(2)
                                )
                            )
                        )
                    ),
                    C1
                ),
                composition(
                    pushed,
                    composition(
                        pushed,
                        composition(
                            pushed,
                            composition(
                                popped,
                                composition(
                                    popped,
                                    P(2)
                                )
                            ),
                            composition(
                                predecessor_of,
                                composition(
                                    last_of,
                                    composition(
                                        popped,
                                        P(2)
                                    )
                                )
                            )
                        ),
                        composition(
                            last_of,
                            composition(
                                popped,
                                P(2)
                            )
                        )
                    ),
                    composition(
                        predecessor_of,
                        composition(
                            last_of,
                            P(2)
                        )
                    )
                )
            )
        )
    ),
    P(3),
    P(1),
    P(2)
)

final_index_of = mu(
    composition(
        logical_not,
        composition(
            is_equal_to,
            composition(
                length_of,
                composition(
                    Ack_seq,
                    P(2),
                    P(3),
                    P(1)
                )
            ),
            C1
        )
    )
)

Ack = composition(
    subscript,
    composition(
        Ack_seq,
        P(1),
        P(2),
        composition(
            final_index_of,
            P(1),
            P(2)
        )
    ),
    C0
)
