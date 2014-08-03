__author__ = 'hooda'

import tools


# First triangle number with n factors.
def trifecta(n):
    """

    :type n: int
    """
    cand = 0
    i = 1
    cand_count = 0
    while not cand_count > n:
        cand += i
        i += 1
        cand_count = len(tools.factors(cand))
    return cand


print(trifecta(500))