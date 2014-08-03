__author__ = 'hooda'

# 1001th prime
#TODO a better(faster) method to find the nth prime no.
import tools


def f(x):
    print((tools.sieve(x))[10000])


f(200000)