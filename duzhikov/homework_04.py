import json


def ll2dict(lst):
    return {sublst[1]: sublst[0] for sublst in lst if len(sublst) >= 2}


class Student:
    def __init__(self, first_name, second_name, major_subject):
        self.first_name = first_name
        self.second_name = second_name
        self.major_subject = major_subject

    def print_info(self):
        print(f"Name: {self.first_name} "
              f"Surname: {self.second_name} "
              f"Major: {self.major_subject}")


def print_student(*args, major_subject='engineering'):
    if len(args) == 2:
        first_name, second_name = args
        student = Student(first_name, second_name, major_subject)
        student.print_info()
    elif len(args) == 1:
        student = args[0]
        student.print_info()
    else:
        print("Invalid number of arguments")


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price}"


class Basket:
    def __init__(self):
        self.items = []
        self.total_price = 0.0

    def __add__(self, item):
        self.items.append(item)
        self.total_price += item.price
        return self

    def __sub__(self, item):
        self.items.remove(item)
        self.total_price -= item.price
        return self

    def __str__(self):
        item_strings = [str(item) for item in self.items]
        item_strings.append(f"Total: {self.total_price:.2f}")
        return " ".join(item_strings)


class DB:
    def __init__(self, filename):
        self.filename = filename
        self.data = {}

    def __enter__(self):
        try:
            with open(self.filename) as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {}
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)

    def list(self):
        return list(self.data.keys())

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)


def bread(func):
    def wrapper(what):
        print("bread")
        func(what)
        print("bread")
    return wrapper


def mayonnaise(func):
    def wrapper(what):
        print("mayonnaise")
        func(what)
    return wrapper


def vegitables(func):
    def wrapper(what):
        print("tomatos")
        func(what)
        print("salad")
    return wrapper
