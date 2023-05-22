class MyDefaultDict(dict):
    def __init__(self, default_factory):
        self.default_factory = default_factory

    def __getitem__(self, key):
        if key not in self:
            self[key] = self.default_factory()
        return super().__getitem__(key)


def my_cache(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = args + tuple(kwargs.items())
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper


def my_partial(func, *args, **kwargs):
    def wrapper(*more_args, **more_kwargs):
        updated_args = args + more_args
        updated_kwargs = kwargs.copy()
        updated_kwargs.update(more_kwargs)
        return func(*updated_args, **updated_kwargs)

    return wrapper
