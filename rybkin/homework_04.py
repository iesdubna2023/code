from typing import Union
from pathlib import Path
import json

lst = [["foo", "bar", "baz"],
       ["Alice", "Reed", "Brittany", "White"],
       [],
       ["Hello"]]


class Student:
    def __init__(self, first_name, second_name, major_subject):
        self.first_name = first_name
        self.second_name = second_name
        self.major_subject = major_subject

    def print(self):
        print(f"Name: {self.first_name} Surname: "
              f"{self.second_name} Major: "
              f"{self.major_subject}")


def ll2dict(lst_: list):
    return {inner_lst[1]: inner_lst[0] for inner_lst
            in lst_ if len(inner_lst) >= 2}


def student_info(student: Union[Student, str], major_subject="engineering"):
    if isinstance(student, Student):
        student.print()
    elif isinstance(student, str):
        if len(student.split()) == 2:
            Student(*student.split(), major_subject).print()
    else:
        raise ValueError("Некорректные данные.")


class Item:
    """
    Класс для абстрактного предмета,
    содержащего значение item - имя и value - цена
    """
    __slots__ = "item_value"

    def __init__(self, item: str, value: float):
        self.item_value: dict = {item: value}

    def __iter__(self):
        yield self.item_value


class Busket:
    """
    Класс для абстрактной корзины,
    содержащей предметы класса Item
    """
    __slots__ = "__items"

    def __init__(self):
        self.__items = []

    def __add__(self, other: Item):
        self.__items.append(other)
        return self

    def __len__(self):
        return len(self.__items)

    def __sub__(self, other):
        if other not in self.__items:
            raise ValueError("Данного предмета нет в корзине.")
        self.__items.remove(other)
        return self

    def __str__(self):
        return " ".join([f"{key}: {value}"
                         for item in self.__items
                         for key, value in item.item_value.items()]) + \
    f" Total {sum([v for i in self.__items for k, v in i.item_value.items()])}"

    def __contains__(self, item):
        return item in self.__items

    def __iter__(self):
        for item in self.__items:
            yield item.item_value


class DB:
    """
    Класс для работы с базой данных на основе json file
    """
    __slots__ = "path", "__data"

    def __init__(self, db_path: str):
        self.path: Path = self._is_correct_path(db_path)
        self.__data = None

    def __enter__(self):
        """Вход в DB"""
        with open(self.path, "r") as file:
            self.__data = json.loads(file.read())
        return self

    def __exit__(self, exc_code, exc_type, traceback):
        """Выход из DB"""
        with open(self.path, "w") as file:
            file.write(json.dumps(self.__data))

    def __iter__(self):
        for key in self.__data:
            yield {key, self.__data.get(key)}

    def _is_correct_path(self, path: str):
        """Проверка на наличие файла по пути"""
        file_path = Path(path)
        if file_path.exists() and file_path.suffix == ".json":
            return file_path
        raise FileNotFoundError("Данный файл не найден.")

    def list(self) -> list:
        """список доступных ключуй"""
        return list(self.__data.keys())

    def set(self, key, value):
        """Внести в json DB"""
        self.__data[key] = value

    def get(self, key):
        """Получить из DB по ключу"""
        return self.__data.get(key)


def bread(func):
    """декоратор хлебушка"""

    def wrapper(*args, **kwargs):
        print("bread")
        func(*args, **kwargs)
        print("bread")

    return wrapper


def mayonnaise(func):
    """декоратор мазика"""
    def wrapper(*args, **kwargs):
        print("mayonnaise")
        func(*args, **kwargs)
    return wrapper


def vegitables(func):
    """декоратор овощей"""
    def wrapper(*args, **kwargs):
        print("tomatos")
        func(*args, **kwargs)
        print("salad")
    return wrapper


# 1
print(ll2dict(lst))
# 2
stud = Student("Ivan", "Rybkin", "cleaner")
student_info(stud)
student_info("Ivan Rybkin", "ingeneer")
# 3
busket = Busket()
tomato = Item("tomato", 1.55)
banana = Item("banana", 2.12)
vine = Item("vine", 14.90)
busket + tomato + banana + vine
print(busket)
busket - vine
print(busket)
# 4
with DB("data.json") as db:
    print(db.path)
    print(db.list())
    db.set("first_name", "Alice")
    db.set("second_name", "Reed")
    print(db.get("second_name"))
    for e in db:
        print(e)
# 5


@bread
@mayonnaise
@vegitables
def sandwich(what):
    print(what)


sandwich("ham")
