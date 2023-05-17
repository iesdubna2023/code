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


def CACHE(fun):
    CachedDict = {}

    def func(*args):
        if CachedDict.get(args) is None:
            CachedDict[args] = fun(*args)
        return CachedDict[args]

    return func


def partial(func, *args):
    def newfunc(*fargs):
        return func(*args, *fargs)

    newfunc.func = func
    newfunc.args = args
    return newfunc
