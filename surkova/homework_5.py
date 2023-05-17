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
    cache_dict = {}

    def wrapper(*args):
        if args in cache_dict:
            return cache_dict[args]
        result = func(*args)
        cache_dict[args] = result
        return result

    return wrapper


def partial(func, *args):
    def newfunc(*fargs):
        return func(*args, *fargs)
    newfunc.func = func
    newfunc.args = args
    return newfunc
