""" Do your best to define these functions.
    Bonus points if you can refactor them into
    an object that handles a list as init variable """


def mean(lst):
    """ returns mean """
    pass

assert mean([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 4.5


def median(lst):
    """ returns median """
    pass

assert median([0, 1, 2, 5, 6, 8]) == 3.5
assert median([0, 3, 5, 8, 100]) == 5


def mode(lst):
    """ returns list of modes or None """
    pass

assert mode([0, 1, 1, 1, 3, 6]) == [1, ]
assert mode([0, 1, 2, 2, 5, 5]) == [2, 5]
assert mode(range(100)) == None


def my_max(lst):
    """ returns max """
    pass

assert my_max([0, 10, 39, 1000]) == 1000
assert my_max([0, 100, 100]) == 100


def my_min(lst):
    """ returns min """
    pass

assert my_min([0, 5, 10]) == 0
assert my_min([-1000, 1000, 0]) == -1000


def quartile(lst):
    """ returns 4 equal sized list """
    pass

assert quartiles(range(16)) == [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]


def interquartile_range(lst):
    """ returns interquartile range """
    pass

assert interquartile_range(range(16)) == range(4, 12)


def standard_deviation(lst):
    """ returns standard deviation """
    pass

assert standard_deviation([10,20,20,50]) == 15


def variance(lst):
    """ returns variance """
    pass

assert variance([1,5,9,100]) == 1620.1875


def standard_error(lst):
    """ returns standard error """
    pass

assert round(standard_error([1,5,19,100]), 2) == 23.24


def covariance(lst1, lst2):
    """ returns covariance of two lists """
    # How would an object handle this?
    pass

assert covariance([1,2,3], [4,5,9]) == 2.5


def correlation(lst1, lst2):
    """ returns correlation of two lists """
    # How would an object handle this?
    pass

assert correlation([1,2,3], [4,5,3]) == -0.5
assert correlation([1,2,3], [1,2,3]) == 1
