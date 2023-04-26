import json
import os.path


def ll2dict(lists):
    return {lst[1]: lst[0] for lst in (lists) if len(lst) > 1}


class Student:
    def __init__(self, first_name, second_name, major_subject):
        self.first_name = first_name
        self.second_name = second_name
        self.major_subject = major_subject

    def print(self):
        print(f"Name: {self.first_name}", end=' ')
        print(f"Surname: {self.second_name}", end=' ')
        print(f"Major: {self.major_subject}")


def print_student(*args):
    if isinstance(args[0], Student):
        args[0].print()
    else:
        first_name = args[0]
        second_name = args[1]
        major_subject = args[2] if len(args) > 2 else "engineering"
        student = Student(first_name, second_name, major_subject)
        student.print()


class Busket():
    def __init__(self):
        self.items = []

    def __add__(self, item):
        if isinstance(item, Item):
            self.items.append(item)
        return self

    def __sub__(self, item):
        if isinstance(item, Item):
            if item in self.items:
                self.items.remove(item)
        return self

    def __str__(self):
        answer = ""
        total_price = 0
        for item in self.items:
            answer += f"{item.name}: {item.price} "
            total_price += item.price

        answer += f"Total: {total_price}"
        return answer


class Item():
    def __init__(self, name, price):
        self.name = name
        self.price = price


class DB():
    def __init__(self, filename):
        self.filename = filename
        self.data = {}
        if not os.path.isfile(self.filename):
            with open(self.filename, 'w') as f:
                f.write(json.dumps(self.data))
        else:
            with open(self.filename, 'r') as f:
                self.data = json.loads(f.read())

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        with open(self.filename, 'w') as f:
            f.write(json.dumps(self.data))

    def list(self):
        return self.data.keys()

    def get(self, key):
        return self.data[key]

    def set(self, key, value):
        self.data[key] = value


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
