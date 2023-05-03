# Практика работы со встроенными возможностями Python

1. Реализовать функцию `ll2dict` которая по заданному списку списков при помощи *dict comprehension*  создает словарь, ключами в котором являются вторые элементы в списках, а значениями первые элементы в списках.

Например, пусть задан список списков
```python
[
    ["foo", "bar", "baz"],
    ["Alice", "Reed", "Brittany", "White"],
    [],
    ["Hello"],
]
```
Функция должна вернуть словарь вида
```python
{
    "bar": "foo",
    "Reed": "Alice",
}
```

1. Используя возможности именованных аргументов, нужно создать функцию `print_student`, принимающую либо имя и фамилию либо объект типа `Student`. Если функции переданы имя и фамилия, то функция должна инициализировать объект типа `Student` и вызывать у него метод `print`. Если передан объект типа `Student`, то функция должна просто вызывать у него метод `print`. Также функция должна опционально принимать параметр, задающий специализацию студента, по умолчанию это должно быть `engineering`.

Задан следующий класс, функцию `print_student` нужно определить самостоятельно
```python
class Studend:
    def __init__(self, first_name, second_name, major_subject):
        self.first_name = first_name
        self.second_name = second_name
        self.major_subject = major_subject
    def print(self):
        print(f"Name: {self.first_name} Surname: {self.second_name} Major: {self.major_subject}")
```

1. Реализовать классы `Item` и `Busket` (товар и корзина для супермаркета). Нужно, чтобы можно было этими классами пользоваться вот так
```python
busket = Busket()
tomato = Item("tomato", 1.55)
banana = Item("banana", 2.12)
vine = Item("vine", 14.90)

busket + tomato + banana + vine
print(busket)
busket - vine
print(busket)
```
Для того чтобы работали `+` и `-` у класса `Busket` нужно реализовать magic методы `__add__` и `__sub__`. Нужно, чтобы при вызове `print(busket)` печаталась строка вида (см. ниже), следовательно также нужно реализовать magic метод `__str__`.
```
tomato: 1.55 banana: 2.12 vine: 14.9 Total: 18.57
```

1. Реализовать простейшую key-value базу данных в виде контекстного менеджера `DB`. Нужно, чтобы при входе в блок `with` файл базы данных читался с диска если он существует, а при выходе из блока `with` данные бы сохранялись в файл на диск. У класса `DB` среди прочего должны быть реализованы методы `list` - чтобы получить список доступных ключей, `set` - установить ключ-значение, `get` - получить значение по ключу.
```python
with DB("db.json") as db:
    print(db.list())
    db.set("first_name", "Alice")
    db.set("second_name", "Reed")
    print(db.get("second_name"))
```
*Подсказка: для того чтобы сериализовывать/десериализовывать базу данных в файл json, можно воспользоваться библиотекой `json`*
```python
import json
d = {
    "key_0": "value_0",
    "key_1": "value_1",
}
# запись словаря в файл
with open("file.json", 'w') as f:
    f.write(json.dumps(d))

# чтение словаря из файла
with open("file.json") as f:
    dd = json.loads(f.read())
```

1. Реализовать декораторы `bread`, `mayonnaise`, `vegitables` для приготовления сендвича с заданной начинкой.
Пример использования этих декоратов
```python
@bread
@mayonnaise
@vegitables
def sandwich(what):
    print(what)

sandwich("ham")
```
При вызове функции `sandwich("ham")` нужно, чтобы печаталось
```
bread
mayonnaise
tomatos
ham
salad
bread
```
