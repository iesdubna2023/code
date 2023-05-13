import functools


class MyDefaultDict(dict):
    def __init__(self, default_factory=None, *args, **kwargs):
        if default_factory and not callable(default_factory):
            raise TypeError("first argument must be callable")
        super().__init__(*args, **kwargs)
        self.default_factory = default_factory

    def __missing__(self, key):
        if self.default_factory is not None:
            self[key] = self.default_factory()
            return self[key]
        else:
            raise KeyError(key)


class MyCache:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value

    def __get__(self, instance, owner):
        return functools.partial(self, instance)


def partial(func, *args, **kwargs):
    def wrapper(*args2, **kwargs2):
        return func(*args, *args2, **kwargs, **kwargs2)
    return functools.update_wrapper(wrapper, func)
