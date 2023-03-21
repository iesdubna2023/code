def reverse(arg):
    result = []
    for i in arg:
        result.insert(0, i)
    return result


def avglen(arg):
    sum([len(i) for i in arg])/len(arg)
    return sum([len(i) for i in arg])/len(arg)


def index(arg):
    result = {}
    for i, word in enumerate(arg):
        if word in result:
            result[word].append(i)
        else:
            result[word] = [i]
    for i in result.keys():
        if len(result[i]) == 1:
            copy = result[i][0]
            result[i] = copy
    return result


def coincidence(arg1, arg2):
    result = []
    for element in arg1:
        if element in arg2 and element not in result:
            result.append(element)
    return result


def count(arg):
    result = {}
    for i in set(arg):
        result[i] = arg.count(i)
    return result


def lensort(arg):
    return sorted(arg, key=len)
