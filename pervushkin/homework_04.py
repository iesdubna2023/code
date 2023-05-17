import json


def ll2dict(arg):
    return {i[1]: i[0] for i in arg if len(i) >= 2}


class Student:
    def __init__(self, first_name, second_name, major_subject):
        self.first_name = first_name
        self.second_name = second_name
        self.major_subject = major_subject

    def print(self):
        print(f"Name: {self.first_name} Surname: {self.second_name} "
              f"Major: {self.major_subject}")


def print_student(first_name='', second_name='', major_subject='engineering',
                  student=None):
    if student is not None:
        student.print()
        return
    elif first_name != '' and second_name != '':
        a = Student(first_name, second_name, major_subject)
        a.print()
        return
    raise Exception('you are not sure')


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Busket:
    def __init__(self):
        self.items = []

    def __add__(self, item):
        self.items.append(item)
        return self

    def __sub__(self, item):
        self.items.remove(item)
        return self

    def __str__(self):
        total_price = sum(item.price for item in self.items)
        items_str = "\n".join(f"{item.name}: "
                              f"{item.price:.2f}"
                              for item in self.items)
        return f"Items in the busket:\n{items_str}" \
               f"\nTotal price: {total_price:.2f}"


class DB:
    def __init__(self, filename):
        self.filename = filename
        try:
            with open(self.filename) as f:
                self.data = json.loads(f.read())
        except FileNotFoundError:
            self.data = {}

    def list(self):
        return list(self.data.keys())

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.filename, 'w') as f:
            f.write(json.dumps(self.data))


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
