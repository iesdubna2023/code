import functools

# Реализация collections.defaultdict


class DefaultDict:

    def __init__(self, default_factory=None):
        self.default_factory = default_factory
        self.dict = {}

    def __getitem__(self, key):
        try:
            return self.dict[key]
        except KeyError:
            if self.default_factory is not None:
                value = self.default_factory()
                self.dict[key] = value
                return value
            else:
                raise

    def __setitem__(self, key, value):
        self.dict[key] = value

    def __repr__(self):
        return f"DefaultDict({self.default_factory}, {self.dict})"


# Создание defaultdict, возвращающий пустой список
my_dict = DefaultDict(list)
print(my_dict)

# Присваивание значения для несуществующего ключа
my_dict["a"].append(1)
print(my_dict)

# Реализация functools.cache


def my_cache(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper


@my_cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))  # 5
print(fibonacci(10))  # 55


# Реализация functools.partial
def my_partial(func, *args, **kwargs):
    @functools.wraps(func)
    def wrapper(*args2, **kwargs2):
        return func(*args, *args2, **kwargs, **kwargs2)
    return wrapper


def my_func(a, b, c):
    return a + b + c


partial_func = my_partial(my_func, 1, c=3)
print(partial_func(2))  # 6
