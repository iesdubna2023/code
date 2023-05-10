import json


# 1
def dict_comrehension(lst):
    s = {}
    for i in range(len(lst)):
        if len(lst[i]) >= 2:
            s[lst[i][1]] = lst[i][0]

    return s


# 2
class Studend:
    def __init__(self, first_name, second_name, major_subject):
        self.first_name = first_name
        self.second_name = second_name
        self.major_subject = major_subject

    def print(self):
        print(f"Name: {self.first_name} Surname: {self.second_name} Major: {self.major_subject}")


def print_std(*args):
    if len(args) == 1 and type(args[0]) == Studend:
        args[0].print()
    elif len(args) == 2:
        std = Studend(str(args[0]), str(args[1]), 'engineering')
        std.print()
    elif len(args) == 3:
        std = Studend(str(args[0]), str(args[1]), str(args[2]))
        std.print()


# 3
class Busket:
    s = {}
    total = 0

    def __add__(self, other):
        if type(other) == Item:
            self.s[other.name] = other.value
            self.total += other.value
            return self

    def __sub__(self, other):
        if type(other) == Item:
            if other.name in self.s:
                del self.s[other.name]
                self.total -= other.value
                return self

    def __str__(self):
        return f'{self.s} Total: {self.total}'


class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value


# 4
class DB:
    def __init__(self, file_name):
        self.file = file_name

    def __enter__(self):
        try:
            with open(self.file) as f:
                self.data = json.loads(f.read())
        except FileNotFoundError:
            self.data = {}
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.file, 'w') as f:
            f.write(json.dumps(self.data))

    def list(self):
        return list(self.data.keys())

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data[key]


# 5
def bread(inside):
    def func(item):
        print("bread")
        inside(item)
        print("bread")

    return func


def mayonnaise(inside):
    def func(item):
        print("mayonnaise")
        inside(item)

    return func


def vegitables(inside):
    def func(item):
        print("tomatos")
        inside(item)
        print("salad")

    return func


@bread
@mayonnaise
@vegitables
def sandwich(item):
    print(item)
