from unification.match import *

def inc(x):
    return x + 1

def dec(x):
    return x - 1

def test_simple():

    d = Dispatcher('d')

    d.add((1,), inc)
    d.add((10,), dec)

    d(1) == 2
    d(10) == 9

