import json


def ll2dict(arg):
    return {i[1]: i[0] for i in arg if len(i) >= 2}


class Studend:
    def __init__(self, first_name, second_name, major_subject):
        self.first_name = first_name
        self.second_name = second_name
        self.major_subject = major_subject

    def print(self):
        print(f"Name: {self.first_name} Surname: {self.second_name} "
              f"Major: {self.major_subject}")


def print_student(first_name='', second_name='',
                  major_subject='engineering', student=None):
    if student is not None:
        student.print()
        return
    elif first_name != '' and second_name != '':
        Studend(first_name, second_name, major_subject).print()
        return
    raise Exception("No arguments")


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Basket:
    def __init__(self):
        self.items = {}

    def __add__(self, item):
        if item.name in self.items:
            self.items[item.name] += item.price
        else:
            self.items[item.name] = item.price
        return self

    def __sub__(self, item):
        if item.name in self.items:
            self.items[item.name] -= item.price
            if self.items[item.name] <= 0:
                del self.items[item.name]
        else:
            raise ValueError(f"{item.name} not in basket")
        return self

    def __str__(self):
        items_str = ", ".join([f"{name}: {price:.2f}" for name,
                               price in self.items.items()])
        total = sum(self.items.values())
        return f"{items_str} Total: {total:.2f}"


class DB:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        try:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {}
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)

    def list(self):
        return list(self.data.keys())

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data[key] if key in self.data else None


def bread(inside):
    def sandwich(what):
        print("bread")
        inside(what)
        print("bread")
    return sandwich


def mayonnaise(inside):
    def sandwich(what):
        print("mayonnaise")
        inside(what)
    return sandwich


def vegetables(inside):
    def sandwich(what):
        print("tomato")
        inside(what)
        print("salad")
    return sandwich


@bread
@mayonnaise
@vegetables
def sandwich(what):
    print(what)
