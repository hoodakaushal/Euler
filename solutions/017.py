__author__ = 'hooda'

words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
         11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
         18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
         70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand', 1000000: 'million',
         1000000000: 'billion', 1000000000000: 'trillion'}


def count_oned():
    s = 0
    for i in range(1, 10):
        s += len(words[i])
    return s


def count_twod():
    ones = count_oned()
    s = ones
    for i in range(10, 20):
        s += len(words[i])
    for i in range(20, 100, 10):
        s += 10 * len(words[i])
        s += ones
    return s


def count_threed():
    twos = count_twod()
    s = twos
    for i in range(100, 1000, 100):
        s += (len(words[i // 100]) + len(words[100])) * 100
        s += len("and") * 99
        s += twos
    return s


print(count_threed() + len("onethousand"))


# TODO create a function to print ARBITRARY naturals in words.
# The challenge here will be the word 'arbitrary'.
# So I have to handle ridiculous stuff like one million billion trillion and twenty two.