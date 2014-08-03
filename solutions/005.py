__author__ = 'hooda'

import tools


def divisible(n):
    """
    Returns the smallest number that is divisible by
    all numbers from 1 to n.

    :type n: int
    :rtype : int
    """
    factors = tools.sieve(n)
    for i in range(0, len(factors)):
        p = factors[i]
        while p * factors[i] <= n:
            p = p * factors[i]
        factors[i] = p
    ans = 1
    for p in factors:
        assert isinstance(p, int)
        ans *= p
    return ans


print(divisible(20))
