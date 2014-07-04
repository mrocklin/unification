from unification.match import *
from unification.utils import raises
from unification.core import var

def inc(x):
    return x + 1


def dec(x):
    return x - 1


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


def foo(*args):
    return args


def test_simple():
    d = Dispatcher('d')

    d.add((1,), inc)
    d.add((10,), dec)

    assert d(1) == 2
    assert d(10) == 9


def test_complex():
    d = Dispatcher('d')
    x = var('x')
    y = var('y')

    d.add((x,), inc)
    d.add((x, 1), add)
    d.add((x, x), mul)
    d.add((x, (x, x)), foo)

    assert d(1) == 2
    assert d(2) == 3
    assert d(2, 1) == 3
    assert d(10, 10) == 100
    assert d(10, (10, 10)) == (10, (10, 10))
    assert raises(NotImplementedError, lambda : d(1, 2))



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


def test_dispatcher():
    @match(1)
    def fib(x):
        return 1

    @match(0)
    def fib(x):
        return 0


def test_supercedes():
    x, y, z = var('x'), var('y'), var('z')
    assert not supercedes(1, 2)
    assert supercedes(1, x)
    assert not supercedes(x, 1)
    assert supercedes((1, 2), (1, x))
    assert not supercedes((1, x), (1, 2))
    assert supercedes((1, x), (y, z))
    assert supercedes(x, y)
    assert supercedes((1, (x, 3)), (1, y))
    assert not supercedes((1, y), (1, (x, 3)))
