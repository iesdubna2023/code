import json


def ll2dict(arg):
    return {i[1]: i[0]for i in arg if len(i) >= 2}


class Student:
    def __init__(self, first_name, second_name, major_subject):
        self.first_name = first_name
        self.second_name = second_name
        self.major_subject = major_subject

    def p(self):
        print(f"Name: {self.first_name} Surname: "
              f"{self.second_name} Major: {self.major_subject}")


def print_student(first_name='', second_name='',
                  major_subject='engineering', student=None):
    if student is not None:
        student.p()
        return
    elif first_name != '' and second_name != '':
        g = Student(first_name, second_name, major_subject)
        g.p()
        return

    raise Exception("No arguments")


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price


class Basket:
    def __init__(self, *all_items):
        self.items = [i for i in all_items]

    def __add__(self, item):
        self.items.append(item)
        return self

    def __sub__(self, item):
        copy = self.items.copy()
        self.items.clear()
        for i in copy:
            if i.name == item:
                continue
            self.items.append(i)
        return self

    def __str__(self):
        result = ""
        summ = 0
        for i in self.items:
            summ += i.price
            result += f"{i.name}: {i.price} "
            result += f"Total: {summ}"
        return result


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


def vegetables(inside):
    def func(item):
        print("tomatoes")
        inside(item)
        print("salad")

    return func


@bread
@mayonnaise
@vegetables
def sandwich(item):
    print(item)
