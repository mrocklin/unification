from .core import unify

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

