__author__ = 'hooda'
from math import factorial


# Number of non-backtracking routes from top left to bottom right in a n by n grid.
def grid_routes(n):
    # (2n!)/(n! * n!)
    return (factorial(2*n))//(factorial(n)**2)

print(grid_routes(20))