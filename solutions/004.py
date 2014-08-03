import tools


def largestpalindrome(x):
    """
    Return the largest palindromic number such that it is the product of two numbers <= x.
    :param x:
    :rtype : int
    """
    i = x
    largest = 0
    while i >= 0:
        j = i
        while j >= 1:
            cand = i * j
            if tools.ispalindrome(str(cand)) and largest < cand:
                largest = cand
            j -= 1
        i -= 1

    return largest


print(largestpalindrome(999))