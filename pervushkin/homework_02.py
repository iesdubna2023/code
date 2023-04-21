def reverse(arg):
    result = []
    for i in range(len(arg)):
        result.append(arg[len(arg) - 1 - i])
    return result


def avglen(arg):
    summa = 0
    for i in arg:
        summa = summa + len(i)
    return summa / len(arg)


def index(arg):
    result = {}
    for i in range(len(arg)):
        if arg[i] not in result.keys():
            result[arg[i]] = [i]
        else:
            result[arg[i]].append(i)
    for i in result.keys():
        if len(result[i]) == 1:
            result[i] = result[i][0]
    return result


def coincidence(arg1, arg2):
    match = set(arg2)
    result = [item for item in arg1 if item in match]
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
    n = len(arg)
    for i in range(n):
        for j in range(i + 1, n):
            if len(arg[i]) > len(arg[j]):
                temp = arg[i]
                arg[i] = arg[j]
                arg[j] = temp
    return arg
