from unification.match import *
from unification.utils import raises

def inc(x):
    return x + 1


def dec(x):
    return x - 1


def test_simple():
    d = Dispatcher('d')

    d.add((1,), inc)
    d.add((10,), dec)

    assert d(1) == 2
    assert d(10) == 9


def test_raises_error():
    d = Dispatcher('d')

    assert raises(NotImplementedError, lambda : d(1, 2, 3))



def test_register():
    d = Dispatcher('d')

    @d.register(1)
    def f(x):
        return 10

    @d.register(2)
    def f(x):
        return 20

    assert d(1) == 10
    assert d(2) == 20
