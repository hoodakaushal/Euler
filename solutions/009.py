__author__ = 'hooda'


# So, here's the idea :
# a+b+c = 1000
# a2 + b2 = c2
# let
# a = r2 - s2
# b = 2rs
# c = r2 + s2
#
# a + b + c = 1000
# => 2r(r+s) = 1000
# A bit of trial and error gives r = 20, s = 5 (note that we need r>=s)
# Which gives a = 375, b = 200, c = 425

# TODO A code to solve 2r(r+s) = n in the general case. But is it really worth it?