__author__ = 'hooda'


# The idea is this : We have to find the path from top to bottom, (using only adjacent numbers when stepping down)
# that has the largest sum. The crux is to notice that we can to this starting from the bottom.
# Suppose we have reached the first floor of the pyramid,
# then to maximise the sum, we must choose the maximum of the two numbers below us.
# Hence, we can replace that number by that number + max of the numbers adjacent to it on the lower level.
# If we do this for the entire first floor, we are left with a shorter pyramid (1 less level).
# This smells of recursion...
# With each recursion, we shorten the pyramid until there is one single number. By the above reasoning,
# that must be the sum of the path with the largest sum.


def pathfinder(pyramid):
    """
    :rtype : int
    :param pyramid: This has to be a list of int lists. The length of the lists should be 1,2,3,4....
    """
    if len(pyramid) == 1:
        return pyramid[0][0]
    else:
        return pathfinder(reducer(pyramid))


def reducer(pyramid):
    depth = len(pyramid)
    depth -= 2
    for i in range(0, len(pyramid[depth])):
        pyramid[depth][i] += max(pyramid[depth + 1][i], pyramid[depth + 1][i + 1])
    return pyramid[:-1]


mypyramid = [[75],
             [95, 64],
             [17, 47, 82],
             [18, 35, 87, 10],
             [20, 4, 82, 47, 65],
             [19, 1, 23, 75, 3, 34],
             [88, 2, 77, 73, 7, 63, 67],
             [99, 65, 4, 28, 6, 16, 70, 92],
             [41, 41, 26, 56, 83, 40, 80, 70, 33],
             [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
             [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
             [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
             [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
             [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
             [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

print(pathfinder(mypyramid))