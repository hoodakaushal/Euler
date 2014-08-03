__author__ = 'hooda'


# Computed will be a dictionary containing lengths of the collatz sequences for various numbers.
# Increment will add the (i,len(collatz i)) entry to computed.)
def increment(x, computed):
    c = [x]
    ans = 1
    while not (c[-1] == 1):
        if c[-1] in computed:
            ans = len(c) + computed[c[-1]] - 1
            c = [1]
        elif c[-1] % 2 == 0:
            c += [c[-1] // 2]
        else:
            c += [3 * c[-1] + 1]
    computed[x] = max(len(c), ans)
    return computed


def longest_collatz(n):
    """


    :rtype : int
    :param n:
    :return: The number <=n with the longest collatz sequence.
    """
    longest = 0
    longest_gen = 0
    computed = {}
    for i in range(1, n):
        computed = increment(i, computed)
        if computed[i] > longest:
            longest = computed[i]
            longest_gen = i
    return longest_gen


print(longest_collatz(1000000))
