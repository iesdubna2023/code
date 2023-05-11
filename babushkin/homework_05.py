import functools


class DefaultDict(dict):
    def __init__(self, default_factory=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default_factory = default_factory

    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except KeyError:
            return self.default_factroy()


def cache(func):
    known_results = {}

    def wrapper(*args, **kwargs):
        arguments = str(args) + str(kwargs)
        if arguments in known_results:
            return known_results[arguments]
        result = func(*args, **kwargs)
        known_results[arguments] = result
        return result
    return wrapper


def partial(func, *args, **kwargs):
    return functools.partial(func, *args, **kwargs)
