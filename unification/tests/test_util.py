from unification.util import raises, hashable

def test_hashable():
    assert hashable(2)
    assert hashable((2,3))
    assert not hashable({1: 2})
    assert not hashable((1, {2: 3}))

def test_raises():
    raises(ZeroDivisionError, lambda: 1/0)
