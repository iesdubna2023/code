import json


def ll2dict(arg):
    return {i[i]: i[0]for i in arg if len(1) >= 2}


class Student:
    def init(self, first_name, second_name, major_subject):
        self.first_name = first_name
        self.second_name = second_name
        self.major_subject = major_subject

    def print(self):
        print(f"Name: {self.first_name}"
              + f"Surname: {self.second_name}"
              + f"Major: {self.major_subject}")


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

    def __repr__(self):
        return f"{self.name}: {self.price}"


class Busket:
    def __init__(self):
        self.items = []
        self.total = 0

    def __add__(self, item):
        self.items.append(item)
        self.total += item.price
        return self

    def __sub__(self, item):
        self.items = [x for x in self.items if x != item]
        self.total -= item.price
        return self

    def __str__(self):
        items_str = " ".join([str(x) for x in self.items])
        return f"{items_str} Total: {self.total:.2f}"


busket = Busket()
tomato = Item("tomato", 1.55)
banana = Item("banana", 2.12)
vine = Item("vine", 14.90)

busket + tomato + banana + vine
print(busket)
busket - vine
print(busket)


class DB:
    def __init__(self, filename):
        self.filename = filename
        with open(self.filename, "r") as file:
            self.db = json.load(file)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        with open(self.filename, "w") as file:
            json.dump(self.db, file)

    def list(self):
        return list(self.db.keys())

    def get(self, key):
        return self.db.get(key)

    def set(self, key, value):
        self.db[key] = value


with DB("db.json") as db:
    print(db.list())
    db.set("Reed", "Alice")
    print(db.get("Reed"))


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


@bread
@mayonnaise
@vegitables
def sandwich(what):
    print(what)


sandwich("ham")
