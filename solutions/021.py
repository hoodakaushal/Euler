__author__ = 'hooda'

import tools


def amicables(n):
    ans = 0
    sumdivs = {}
    for i in range(1, n + 1):
        sumdivs[i] = sum(tools.factors(i)[:-1])
    print(sumdivs)
    for i in range(1, len(sumdivs)):
        j = sumdivs[i]
        if not (j in sumdivs):
            sumdivs[j] = sum(tools.factors(j)[:-1])
        if (i == sumdivs[j]):
            print(i, sumdivs[i])
            ans += (i + sumdivs[i])
    return ans


print(amicables(10000))