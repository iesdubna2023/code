def reverse(arg):
    result = []
    for v in arg:
        result.insert(0, v)
    return result

def avglen(arg):
    sum = 0
    for v in arg:
        sum += len(v)
    return sum / len(arg)

def index(arg):
    result = {}
    for i, v in enumerate(arg):
        if v not in result.keys():
            result[v] = [i]
        else:
            result[v].append(i)
    return result

def coincidence(arg1, arg2):
    result = []
    for v in arg1:
        if v not in result:
            if v in arg2:
                result.append(v)
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
    l = len(result)
    for i in range(l - 1):
        for j in range(l - i - 1):
            if len(result[j]) > len(result[j + 1]):
                copy = result[j]
                result[j] = result[j + 1]
                result[j + 1] = copy
    return result
