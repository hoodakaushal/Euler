import math


def ispalindrome(s):
    """
    Return True if the input is palindromic.
    :param s: String, list or tuple.
    :rtype : bool
    """
    while len(s) > 0 and s[0] == s[-1]:
        s = s[1:-1]
    if len(s) == 0:
        return True
    return False


def sieve(x):
    """
    Returns list of primes up to x.
    :type x: int
    """
    ar = [False] * 2 + [True] * (x - 1)
    for i in range(2, x):
        if ar[i]:
            j = 2
            while x >= i * j:
                ar[i * j] = False
                j += 1
    primes = []
    for i in range(2, x):
        if ar[i]:
            primes += [i]
    return primes


def factors(x):
    f = []
    int_root = int(math.sqrt(x))
    for i in range(1, int_root + 1):
        q = x // i
        if i * q == x:
            f += [i, q]
    return list(set(f))


# TODO Is it possible to maintain a rolling list of product, so that we get better efficiency?
def max_product(num_ar, k):
    """
    :rtype : int
    :param num_ar: List of numbers.
    :param k: The no. of consecutive numbers whose maximum product will be calculated.
    :return: The largest product of k consecutive numbers in num_ar. If k > len(num_ar), returns 0.
    """
    global cand
    ans = 0
    for i in range(k - 1, len(num_ar)):
        cand = 1
        for j in range(0, k):
            cand = cand * num_ar[i - j]
        if cand > ans:
            ans = cand
    return ans


def matrix_diagonalise(m):
    """
    Return a list of the diagonals of the matrix.
    Diagonals are oriented downwards and right(like the line x+y = 0)
    To be honest, diagonals are kind of messy and undefined for non-square matrices, so use at your own risk,
    because it may not return what you think it should return.
    :rtype : list(int list)
    :param m: A matrix
    """
    if len(m) == 0:
        return m
    rows = len(m)
    columns = len(m[0])
    d = []
    i = rows - 1
    while i >= 0:
        diag = get_diagonal(m, i, 0)
        d += [diag]
        i -= 1
    if columns > 1:
        for j in range(1, columns):
            diag = get_diagonal(m, 0, j)
            d += [diag]
    return d


def get_diagonal(m, i, j):
    diag = []
    rows = len(m)
    columns = len(m[0])
    while 0 <= i < rows and 0 <= j < columns:
        diag += [m[i][j]]
        i += 1
        j += 1
    return diag


# TODO find out why t = [[0]*3]*3 seems to link the rows together,
# so that t[0][0] = 1 makes the first element of every row 1.
def matrix_transpose(m):
    if len(m) == 0:
        return m
    rows_old = len(m)
    columns_old = len(m[0])
    transposed = []
    for i in range(0, columns_old):
        r = []
        for j in range(0, rows_old):
            r += [m[j][i]]
        transposed += [r]
    return transposed