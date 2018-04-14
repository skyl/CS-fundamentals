"""
Return the set of all subsets

For example:

[1, 2, 3] => {
    {}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}
}
"""

import itertools


# TODO: hrm. make my own solution; understand this code better;
# make a recursive solution?
# https://docs.python.org/2/library/itertools.html#itertools.combinations
def my_combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))

    # yield the first r elements of the iterable
    yield tuple(pool[i] for i in indices)

    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            # no break in for loop
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)


def super_set(input, combinations=itertools.combinations):
    result = set()
    for i in range(len(input) + 1):
        for s in combinations(input, i):
            result.add(s)

    return result
