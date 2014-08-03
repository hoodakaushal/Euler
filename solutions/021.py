__author__ = 'hooda'

import tools


def amicables(n):
    ans = 0
    sumdivs = {}
    for i in range(1, n + 1):
        sumdivs[i] = sum(tools.factors(i)) - i
    print(sumdivs)
    for i in range(1, len(sumdivs)):
        j = sumdivs[i]
        if 1 <= j <= n:
            a = i
            b = sumdivs[i]
            if sumdivs[b] == a and sumdivs[a] == b and not (a == b):
                print(i, sumdivs[i])
                ans += (i + sumdivs[i])
    return ans // 2


print(amicables(10000))