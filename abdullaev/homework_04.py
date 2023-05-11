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


class Basket:
    def init(self):
        self.items = []

    def __add__(self, other):
        self.items.append(other)
        return self

    def __sub__(self, other):
        self.items.remove(other)
        return self

    def __str__(self):
        total_price = sum(item.price for item in self.items)
        item_ns = " ".join(f"{item.name}: {item.price}" for item in self.items)
        return f"{item_ns} Total: {total_price}"


class DB:
    def init(self, filename):
        self.filename = filename
        self.data = {}

    def __enter__(self):
        try:
            with open(self.filename) as f:
                self.data = json.load(f)
        except FileNotFoundError:
            pass
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


def vegitables(func):
    def new_func(what):
        print("tomatos")
        func(what)
        print("salad")
    return new_func


def mayonnaise(func):
    def new_func(what):
        print("mayonnaise")
        return func(what)
    return new_func


def bread(func):
    def new_func(what):
        print("bread")
        func(what)
        print("bread")
    return new_func
