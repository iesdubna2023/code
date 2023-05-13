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


import functools

def my_cache(func):
    results = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = args + tuple(sorted(kwargs.items()))
        if key in results:
            return results[key]
        else:
            result = func(*args, **kwargs)
            results[key] = result
            return result
    return wrapper


import functools

def my_partial(func, *args, **kwargs):
    @functools.wraps(func)
    def wrapper(*args2, **kwargs2):
        all_args = args + args2
        all_kwargs = {**kwargs, **kwargs2}
        return func(*all_args, **all_kwargs)
    return wrapper
