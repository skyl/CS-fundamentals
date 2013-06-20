import random
import functools


# 1.2.6

def random_circular_rotation(s):
    n = random.randrange(len(s))
    return s[n:] + s[:n]


def test_on_idx(idx, t, s):
    to_test = t[idx:] + t[:idx]
    #print "trying", idx, t, to_test
    return s == to_test


def check_lucky_circular_rotation_cases(f):

    @functools.wraps(f)
    def wrapper(s, t):
        if len(s) != len(t):
            return False
        if s == t:
            return True
        return f(s, t)

    return wrapper


@check_lucky_circular_rotation_cases
def is_circular_rotation(s, t):

    # just check each place and find if it is equal
    for n in range(len(s)):
        if test_on_idx(n, t, s):
            return True
    return False


@check_lucky_circular_rotation_cases
def is_circular_rotation2(s, t):

    first = s[0]
    search_idx = 0

    while True:
        idx = t.find(first, search_idx)
        if idx == -1:
            return False
        if test_on_idx(idx, t, s):
            return True
        search_idx = idx + 1


def is_circular_rotation3(s, t):
    return len(t) == len(s) and t in s * 2


# 1.2.7

def mystery(s):
    n = len(s)
    if n <= 1:
        return s

    a = s[0: n / 2]
    b = s[n / 2: n]
    return mystery(b) + mystery(a)


if __name__ == "__main__":
    assert mystery("foobar") == "raboof"
    assert is_circular_rotation("ACTGACG", "TGACGAC")

