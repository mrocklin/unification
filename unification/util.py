from functools import partial
from toolz.compatibility import range, map


def hashable(x):
    try:
        hash(x)
        return True
    except TypeError:
        return False


def transitive_get(key, d):
    """ Transitive dict.get

    >>> d = {1: 2, 2: 3, 3: 4}
    >>> d.get(1)
    2
    >>> transitive_get(1, d)
    4
    """
    while hashable(key) and key in d:
        key = d[key]
    return key


def dicthash(d):
    return hash(frozenset(d.items()))


def raises(err, lamda):
    try:
        lamda()
        raise Exception("Did not raise %s"%err)
    except err:
        pass
