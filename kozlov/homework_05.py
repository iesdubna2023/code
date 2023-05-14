class MyDefaultdict(dict):
    def __init__(self, def_factory=None, def_dict={}, **kwargs):
        if (def_factory is not None and not callable(def_factory)):
            raise TypeError('first argument must be callable')
        super().__init__(self, **kwargs | def_dict)
        self.def_factory = def_factory

    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            return self.__missing__(key)

    def __missing__(self, key):
        if self.def_factory is None:
            raise KeyError(key)
        else:
            self[key] = value = self.def_factory()
            return value


def cache(func):
    cache_dict = {}

    def wrapper(*args):
        if args in cache_dict:
            return cache_dict[args]
        result = func(*args)
        cache_dict[args] = result
        return result

    return wrapper


def partial(func, *args, **kwargs):
    def new_func(*fargs, **fkwargs):
        all_args = list(args)
        all_args.extend(fargs)
        all_kwargs = kwargs.copy()
        all_kwargs.update(fkwargs)
        return func(*all_args, **all_kwargs)
    return new_func
