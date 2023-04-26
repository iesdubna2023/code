def reverse(arg):
    result = []
    for u in arg:
        result.insert(0, u)
    return result


def avglen(arg):
    sred = 0
    for i in arg:
        sred = sred + len(i)
    return sred / len(arg)


def index(arg):
    result = {}
    for i, x in enumerate(arg):
        if x not in result.keys():
            result[x] = [i]
        else:
            result[x].append(i)
    for i in result.keys():
        if len(result[i]) == 1:
            copy = result[i][0]
            result[i] = copy
    return result


def coincidence(arg, arg1):
    sovp = set(arg1)
    result = [item for item in arg if item in sovp]
    return result


def count(arg):
    result = {}
    for i in arg:
        if i not in result.keys():
            result[i] = 1
        else:
            result[i] += 1
    return result


def lensort(arg):
    result = arg
    length = len(result)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if len(result[j]) > len(result[j + 1]):
                copy = result[j]
                result[j] = result[j + 1]
                result[j + 1] = copy
    return result
