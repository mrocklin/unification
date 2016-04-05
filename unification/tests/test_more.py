from collections import namedtuple

from unification.more import (unify_object, reify_object,
        unifiable)
from unification import var, variables
from unification.core import unify, reify, _unify, _reify

class Foo(object):
        def __init__(self, a, b):
            self.a = a
            self.b = b
        def __eq__(self, other):
            return (self.a, self.b) == (other.a, other.b)


class Bar(object):
        def __init__(self, c):
            self.c = c
        def __eq__(self, other):
            return self.c == other.c


def test_unify_object():
    assert unify_object(Foo(1, 2), Foo(1, 2), {}) == {}
    assert unify_object(Foo(1, 2), Foo(1, 3), {}) == False
    assert unify_object(Foo(1, 2), Foo(1, var(3)), {}) == {var(3): 2}


def test_reify_object():
    obj = reify_object(Foo(1, var(3)), {var(3): 4})
    assert obj.a == 1
    assert obj.b == 4

    f = Foo(1, 2)
    assert reify_object(f, {}) is f

def test_reify_slots():

    class SlotsObject(object):
        __slots__ = ['myattr']
        def __init__(self, myattr):
            self.myattr = myattr

    x = var()
    s = {x: 1}
    e = SlotsObject(x)
    assert reify_object(e, s), SlotsObject(1)
    assert reify_object(SlotsObject(1), s), SlotsObject(1)

def test_objects_full():
    _unify.add((Foo, Foo, dict), unify_object)
    _unify.add((Bar, Bar, dict), unify_object)
    _reify.add((Foo, dict), reify_object)
    _reify.add((Bar, dict), reify_object)

    assert unify_object(Foo(1, Bar(2)), Foo(1, Bar(var(3))), {}) == {var(3): 2}
    assert reify(Foo(var('a'), Bar(Foo(var('b'), 3))),
                 {var('a'): 1, var('b'): 2}) == Foo(1, Bar(Foo(2, 3)))


def test_unify_slice():
    x = var('x')
    y = var('y')

    assert unify(slice(1), slice(1), {}) == {}
    assert unify(slice(1, 2, 3), x, {}) == {x: slice(1, 2, 3)}
    assert unify(slice(1, 2, None), slice(x, y), {}) == {x: 1, y: 2}


def test_reify_slice():
    x = var('x')
    assert reify(slice(1, var(2), 3), {var(2): 10}) == slice(1, 10, 3)


@unifiable
class A(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


def test_unifiable():
    x = var('x')
    f = A(1, 2)
    g = A(1, x)
    assert unify(f, g, {}) == {x: 2}
    assert reify(g, {x: 2}) == f


@unifiable
class Aslot(object):
    slots = 'a', 'b'
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


def test_unifiable():
    x = var('x')
    f = Aslot(1, 2)
    g = Aslot(1, x)
    assert unify(f, g, {}) == {x: 2}
    assert reify(g, {x: 2}) == f
