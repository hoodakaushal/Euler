__author__ = 'hooda'


def isleap(year):
    """


    :rtype : bool
    :type year: int
    """
    if year % 100 == 0:
        if year % 400 == 0:
            return True
    elif year % 4 == 0:
        return True
    return False


def days(month, leap):
    """

    :return The number of days in the month.
    :rtype : int
    :param month: Month should be from 1 to 12. Y'know, because it is a month.
    :param leap: Whether the year is a leap year or not.
    :type month: int
    :type leap: bool
    """
    dayslist = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2:
        if leap:
            return 29
        else:
            return 28
    return dayslist[month]


def firstofmonths(jan1, year):
    """
    Returns a tuple consisting of a list of the day for the first of each month in the year
    and an integer which is the day of the first month of jan1 of next year.
    The days are 0 - sunday, 1 - monday ...
    :param jan1: The day on the first of jan of given year.
    :rtype : tuple
    """
    firsts = [-1, jan1]
    leap = isleap(year)
    for i in range(1, 13):
        nextfirst = (days(i, leap) + firsts[-1]) % 7
        firsts += [nextfirst]
    return firsts[0:-1], firsts[-1]


def sundaycounter(begin, end, jan1_begin):
    """

    :rtype : int
    """
    total = 0
    jan1 = jan1_begin
    for i in range(begin, end + 1):
        f = firstofmonths(jan1, i)
        jan1 = f[1]
        for day in f[0][1:]:
            if day == 0:
                total += 1
    return total


jan1_1901 = firstofmonths(1, 1900)[1]
print(sundaycounter(1901, 2000, jan1_1901))
