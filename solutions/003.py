__author__ = 'hooda'


# Largest prime factor of x
def largest_pf(x):
    # Essentially we are prime factorising x.
    # Clearly, since factors are being discovered in increasing order, the final factor is the largest.
    factor = 2
    while x > factor:
        if x % factor == 0:
            x = x // factor
            while x % factor == 0:
                x = x // factor
        else:
            factor += 1
    return factor


print(largest_pf(600851475143))