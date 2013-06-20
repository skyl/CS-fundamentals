# TODO: do the very first bits.
import math
import operator
import timeit


def banner(s):
    print "=============================="
    print s
    print "=============================="


# 1.1.14
########

def lg(num):
    """Returns the largest int not larger than the base-2 log of num"""
    print math.log(num, 2)
    i = 1
    while True:
        # the first i where 2 ** i is greater than num
        # means i - 1
        if 2 ** i > num:
            return i - 1
        i += 1


# 1.1.18
########

def mystery(a, b, op=operator.add):
    print "mystery called with", a, b, op
    if op == operator.add:
        base = 0
    elif op == operator.mul:
        base = 1
    else:
        raise ValueError("operator must be multiplication or addition")

    if b == 0:
        #print "ZERO"
        return base
    if b % 2 == 0:
        #print "EVEN", a, b, op
        return mystery(op(a, a), b / 2, op)
    #print "ODD", a, b, op
    #print mystery(op(a, a), b / 2, op)
    #print a
    ret = op(mystery(op(a, a), b / 2, op), a)
    #print ret
    return ret


def _1_1_18():
    banner("1.1.18")
    print "Using addition with 0"
    print mystery(2, 25)
    print mystery(3, 11)
    print "Using multiplication with 1"
    print mystery(2, 25, operator.mul)
    print mystery(3, 11, operator.mul)


# 1.1.19
#####################

# What is the largest value of n where this will take less than 1 hour?
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def better_fib(n):
    fib_memo = {
        0: 0,
        1: 1,
    }
    if n not in fib_memo:
        fib_memo[n] = better_fib(n - 1) + better_fib(n - 2)
    return fib_memo[n]


def _1_1_19():
    banner("1.1.19")
    print "fibonacci"
    for a in range(11):
        print fibonacci(a)
    print "better_fib"
    for a in range(11):
        print better_fib(a)
    print "fib 30 with recursive", timeit.timeit(
        lambda: fibonacci(30), number=1)
    print "fib 30 with memo", timeit.timeit(lambda: better_fib(30), number=1)
    print better_fib(30)


# 1.1.20
#####################

def naive_factorial(n):
    if n == 0:
        return 1
    return n * naive_factorial(n - 1)


def factorial(n):
    fact_memo = {
        0: 1,
    }

    if n not in fact_memo:
        fact_memo[n] = n * factorial(n - 1)
    return fact_memo[n]


def ln_of_factorial(n):
    """Computes ln (n!) recursively"""
    return math.log(factorial(n))


def _1_1_20():
    pass


def main():
    #_1_1_18()
    #_1_1_19()
    #_1_1_20()
    pass


if __name__ == "__main__":
    main()
