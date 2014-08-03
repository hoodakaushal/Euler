__author__ = 'hooda'


# Sum of even valued fibonacci terms whose value does not exceed x.
def fibsum(x):
    ans = 0
    a, b = 1, 2
    while b <= x:
        ans += b
        #Because only every third fibonacci number after 2 is even. 1,[2],3,5,[8],13,21,[34]...
        a, b = b, a + b
        a, b = b, a + b
        a, b = b, a + b
    return ans


print(fibsum(4000000))