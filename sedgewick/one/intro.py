"""
The beginning of the book :)
"""

def gcd(p, q):
    """Recursive greatest common divisor function"""
    if q == 0:
        return p
    r = p % q
    return gcd(q, r)


def rank(key, arr, lo=0, hi=None):
    """
    recursive implementation of binary search.
    searching for `key` in ordered array, `arr` in range `lo` to `hi`.
    pg. 39
    """
    maxindex = len(arr) - 1
    if hi is None:
        hi = maxindex
    elif hi > maxindex:
        raise ValueError("hi can be no larger than len(arr) - 1")

    if lo > hi:
        # not here!
        return -1

    mid = lo + (hi - lo) / 2

    if key < arr[mid]:
        return rank(key, arr, lo, mid - 1)
    elif key > arr[mid]:
        return rank(key, arr, mid + 1, hi)
    else:
        return mid
