

class defaultdict(dict):
    """
    collections.defaultdict
    """

    def __init__(self, default_factory):
        super().__init__()
        self.default_factory = default_factory

    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        value = self.default_factory()
        self[key] = value
        return value

    def __repr__(self):
        return f"defaultdict({self.default_factory.__name__}, " \
               f"{super().__repr__()})"


def cache(func):
    """functools.cache"""
    memory = {}

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in memory:
            memory[key] = func(*args, **kwargs)
        return memory[key]

    return wrapper


def partial(func, *args, **kwargs):
    """functools.partial"""

    def wrapper(*args_remaining, **kwargs_remaining):
        args_combined = args + args_remaining
        kwargs_combined = {**kwargs, **kwargs_remaining}
        return func(*args_combined, **kwargs_combined)

    return wrapper


# 1. defaultdict
print("Тест 1:")
# Если элемента нет, то он будет по умолчаю того типа, что передан при иниц-ции
d = defaultdict(int)  # <- внутрь можно передать любую функцию или type
print(d[1])
f = defaultdict(float)
print(f[2])


# 2. cache
print("Тест 2:")
# Сохраняет значение вызовов функции. Удобно для рекурсий


@cache
def test_func(n):
    return n * 2


print(test_func(5), test_func(10), test_func(111))
# __closure__ даёт данные о "ячейках" декоратора.
# Контейнер memory лежит в cell_contents ячейки [1]
print(test_func.__closure__[1].cell_contents.values())
# Можно ещё саму функцию вызвать прямо из ячейки
# print(test_func.__closure__[0].cell_contents(6))

# 3. partial
print("Тест 3:")
# Можно сделать new функцию, объявив её на основе старой, ещё и с доп. арг-ми


def xor(a, b):
    """побитный сдвиг a на b"""
    return a ^ b
# Указано, что a по умолчанию = 3


xor1 = partial(xor, 3)
# Передаём b и выводим
print(xor1(124))
# Можно и так
# Передаём при вызове новой функции меньше арг-в на
# столько, сколько указал по умолчанию


def prost(a, b, c, m):
    return a + b + c + m


more_prost = partial(prost, 1, 2)
# Тут по умолчанию указано 2 аргумента. Изначальная функция принимает 4
# Передаём в новую функцию 2 аргумента
print(more_prost(2, 2))
