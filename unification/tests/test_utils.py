from unification.utils import raises, hashable

def test_hashable():
    assert hashable(2)
    assert hashable((2,3))
    assert not hashable({1: 2})
    assert not hashable((1, {2: 3}))

def test_raises():
    assert raises(ZeroDivisionError, lambda: 1/0)
    assert not raises(ZeroDivisionError, lambda: 0/1)
