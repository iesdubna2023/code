import functools


class DefaultDict:
    def __init__(self, func):
        self.func = func
        self.dict = {}

    def get(self, key):
        if key in self.dict:
            return self.dict[key]
        else:
            return self.func()

    def set(self, key, val):
        self.dict[key] = val
        pass


def cache(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper.cache:
            wrapper.cache[cache_key] = func(*args, **kwargs)
        return wrapper.cache[cache_key]
    wrapper.cache = dict()
    return wrapper


def partial(func, *args):
    def newfunc(*fargs):
        return func(*args, *fargs)
    newfunc.func = func
    newfunc.args = args
    return newfunc
