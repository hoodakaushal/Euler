__author__ = 'hooda'


def sumsqdiff(n):
    """
    :return: (Square of sum) - (Sum of squares)
    """
    return (n * (n + 1) * (n - 1) * (3 * n + 2)) // 12


print(sumsqdiff(100))