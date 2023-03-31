def reverse(array):
    a = []
    for i in range(len(array)):
        if i != 0:
            a.append(array[i * -1])
    a.append(array[0])
    return a


def avglen(array):
    s = 0
    k = 0
    for i in range(len(array)):
        a = len(array[i])
        s += a
        k += 1
    return s / k


def index(array):
    dictionary = {}
    for value, key in enumerate(array):
        if key not in dictionary.keys():
            dictionary[key] = [value]
        else:
            dictionary[key].append(value)
    for key in dictionary.keys():
        if len(dictionary[key]) == 1:
            copy = dictionary[key][0]
            dictionary[key] = copy
    return dictionary


def coincidence(array1, array2):
    a = []
    for i in range(len(array1)):
        for j in range(len(array2)):
            if array1[i] == array2[j]:
                a.append(array1[i])
    return a


def count(array):
    dictionary = {}
    for value, key in enumerate(array):
        if key not in dictionary.keys():
            dictionary[key] = 1
        else:
            dictionary[key] += 1
    return dictionary


def lensort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if len(array[j]) > len(array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
