class DefaultDict(dict):
    def __init__(self, default_factory=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default_factory = default_factory

    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except KeyError:
            return self.default_factroy()

    def default_factroy(self):
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
