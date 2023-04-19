# Практика работы со встроенными возможностями Python

- Задан список списков разной длины
```python
[
    ["foo", "bar", "baz"],
    ["Alice", "Reed", "Brittany", "White"],
    [],
    ["Hello"],
]
```
Используя *dict comrehension* нужно создать словарь вида
```python
{
    "bar": "foo",
    "Reed": "Alice",
}
```

- Используя возможности именованных аргументов, нужно создать функцию, принимающую либо имя и фамилию либо объект типа `Student`. Если функции переданы имя и фамилия, то функция должна инициализировать объект типа `Student` и вызывать у него метод `print`. Если передан объект типа `Student`, то функция должна просто вызывать у него метод `print`. Также функция должна опционально принимать параметр, задающий специализацию студента, по умолчанию это должно быть `engineering`.

```python
class Studend:
    def __init__(self, first_name, second_name, major_subject):
        self.first_name = first_name
        self.second_name = second_name
        self.major_subject = major_subject
    def print(self):
        print(f"Name: {self.first_name} Surname: {self.second_name} Major: {self.major_subject}")
```

- Реализовать классы `Item` и `Busket` (товар и корзина для супермаркета). Нужно, чтобы можно было этими классами пользоваться вот так
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
Для того чтобы работали `+` и `-` у класса `Busket` нужно реализовать методы `__add__` и `__sub__`. Нужно, чтобы при вызове `print(busket)` печаталась строка вида (см. ниже), следовательно нужно реализовать метод `__str__`.
```
tomato: 1.55 banana: 2.12 vine: 14.9 Total: 18.57
```

- Реализовать простейшую key-value базу данных в виде контекстного менеджера. Нужно, чтобы при входе в блок `with` файл базы данных читался с диска, а при выходе из блока `with` данные бы сохранялись в файл на диск. У класса DB среди прочего должны быть реализованы методы `list` - чтобы получить список доступных ключей, `set` - установить ключ-значение, `get` - получить значение по ключу.
```python
with DB("db.json") as db:
    print(db.list())
    db.set("Reed", "Alice")
    print(db.get("Reed"))
```

- Реализовать декораторы для приготовления сендвича с заданной начинкой
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
