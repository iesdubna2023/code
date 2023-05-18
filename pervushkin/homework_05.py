class DefaultDict(dict):
    def __init__(self, default_factory):
        super().__init__()
        self.default_factory = default_factory

    def __missing__(self, key):
        self[key] = self.default_factory()
        return self[key]


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
    def new_func(*more_args):
        return func(*args, *more_args)
    return new_func
