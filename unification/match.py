from .core import unify

class Dispatcher(object):
    def __init__(self, name):
        self.name = name
        self.funcs = dict()

    def add(self, signature, func):
        self.funcs[signature] = func

    def __call__(self, *args, **kwargs):
        for k, v in self.funcs.items():
            if unify(k, args):
                return v(*args, **kwargs)
