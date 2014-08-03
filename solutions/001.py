__author__ = 'hooda'


# Sum of numbers that are multiple of 3 or 5 below x.
def multiples(x):
    ans = 0
    for i in range(1, x):
        if i % 3 == 0 or i % 5 == 0:
            ans += i
    return ans


print(multiples(1000))