from .core import unify, reify
from .variable import var, isvar

class Dispatcher(object):
    def __init__(self, name):
        self.name = name
        self.funcs = dict()

    def add(self, signature, func):
        self.funcs[signature] = func

    def __call__(self, *args, **kwargs):
        for k, v in self.funcs.items():
            if unify(k, args) != False:
                return v(*args, **kwargs)
        raise NotImplementedError("No match found")

    def register(self, *signature):
        def _(func):
            self.add(signature, func)
            return self
        return _


global_namespace = dict()


def match(*signature, **kwargs):
    namespace = kwargs.get('namespace', global_namespace)
    def _(func):
        name = func.__name__

        if name not in namespace:
            namespace[name] = Dispatcher(name)
        dispatcher = namespace[name]

        dispatcher.add(signature, func)

        return dispatcher
    return _


def supercedes(a, b):
    """ ``a`` is a more specific match than ``b`` """
    if isvar(b) and not isvar(a):
        return True
    s = unify(a, b)
    if s is False:
        return False
    s = dict((k, v) for k, v in s.items() if not isvar(k) or not isvar(v))
    if reify(a, s) == a:
        return True


# Taken from multipledispatch
def edge(a, b, tie_breaker=hash):
    """ A should be checked before B

    Tie broken by tie_breaker, defaults to ``hash``
    """
    if supercedes(a, b):
        if supercedes(b, a):
            return tie_breaker(a) > tie_breaker(b)
        else:
            return True
    return False


# Taken from multipledispatch
def ordering(signatures):
    """ A sane ordering of signatures to check, first to last

    Topoological sort of edges as given by ``edge`` and ``supercedes``
    """
    signatures = list(map(tuple, signatures))
    edges = [(a, b) for a in signatures for b in signatures if edge(a, b)]
    edges = groupby(lambda x: x[0], edges)
    for s in signatures:
        if s not in edges:
            edges[s] = []
    edges = dict((k, [b for a, b in v]) for k, v in edges.items())
    return _toposort(edges)
