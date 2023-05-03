import json


def ll2dict(arg):
    return {i[i]: i[0]for i in arg if len(1) >= 2}


class Student:
    def __init__(self, first_name, second_name, major_subject):
        self.first_name = first_name
        self.second_name = second_name
        self.major_subject = major_subject

    def print(self):
        print(f"Name: {self.first_name}", end=' ')
        print(f"Surname: {self.second_name}", end=' ')
        print(f"Major: {self.major_subject}")


def print_student(first_name='', second_name='',
                  major_subject='engineering', student=None):
    if student is not None:
        student.print()
        return
    elif first_name != '' and second_name != '':
        sick = Student(first_name, second_name, major_subject)
        sick.print()
        return

    raise Exception()


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price:.2f}"


class Busket:
    def __init__(self):
        self.items = []
        self.total = 0.0

    def __add__(self, item):
        self.items.append(item)
        self.total += item.price
        return self

    def __sub__(self, item):
        self.items = [i for i in self.items if i != item]
        self.total -= item.price
        return self

    def __str__(self):
        items_str = "".join(str(item) for item in self.items)
        return f"{items_str} Total: {self.total:.2f}"


class DB:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = {}

    def __enter__(self):
        try:
            with open(self.file_name) as f:
                self.data = json.load(f)
        except FileNotFoundError:
            pass
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        with open(self.file_name, 'w') as f:
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
        print("mayonnaise")
        return wrapper


def vegetables(func):
    def wrapper(what):
        print("tomatoes")
        func(what)
        print("salad")
        return wrapper
