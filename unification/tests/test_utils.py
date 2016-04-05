from unification.utils import freeze, hashable, raises

def test_hashable():
    assert hashable(2)
    assert hashable((2,3))
    assert not hashable({1: 2})
    assert not hashable((1, {2: 3}))

def test_raises():
    assert raises(ZeroDivisionError, lambda: 1/0)
    assert not raises(ZeroDivisionError, lambda: 0/1)


def test_freeze():
    assert freeze({1: [2, 3]}) == frozenset([(1, (2, 3))])
    assert freeze(set([1])) == frozenset([1])
    assert freeze(([1], )) == ((1, ), )
