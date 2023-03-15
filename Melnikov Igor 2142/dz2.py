# Создать функцию, которая в качестве аргумента принимает список и возвращает его в обратном порядке.

def reverse(arg):
    result = []
    for v in arg:
        result.insert(0, v)
    return result

# Создать функцию, которая принимает список слов и возвращает среднюю длину слов в списке.

def avg_len(arg):
    sum = 0
    for v in arg:
        sum += len(v)
    return sum / len(arg)

# Создать функицию, которая принимает список слов и возвращает словарь,
# в котором заданы порядковые номера слов в списке.

def make_dict(arg):
    result = {}
    for i, v in enumerate(arg):
        if v not in result.keys():
            result[v] = [i]
        else:
            result[v].append(i)
    return result

# Создать функцию, которая принимает два списка и возвращает список из совпадающих элементов (порядок не важен)

def XOR(arg1, arg2):
    result = []
    for v in arg1:
        if v not in result:
            if v in arg2:
                result.append(v)
    return result

# Создать функицию, которая принимает список слов и возвращает словарь, в котором указано количество раз,
# которое то или иное слово встречается.

def count_rep(arg):
    result = {}
    for i in arg:
        if i not in result.keys():
            result[i] = 1
        else:
            result[i] += 1
    return result

# Создать функцию, которая принимает список слов и возвращает список в котором эти слова отсортированы по длине.
# Для слов одинаковой длины, их порядок в результирующем списке не важен.

def len_sort(arg):
    result = arg
    l = len(result)
    for i in range(l - 1):
        for j in range(l - i - 1):
            if len(result[j]) > len(result[j + 1]):
                copy = result[j]
                result[j] = result[j + 1]
                result[j + 1] = copy
    return result