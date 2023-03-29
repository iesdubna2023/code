def reverse(arg):
    result = []
    for v in arg:
        result.insert(0, v)
    return result


def avglen(arg):
    amount = 0
    for v in arg:
        amount += len(v)
    return amount / len(arg)


def index(arg):
    res = {}
    for i in range(len(arg)):
        if arg.count(arg[i]) > 1:
            res[arg[i]] = []
        else:
            res[arg[i]] = 0
    for i in range(len(arg)):
        if type(res[arg[i]]) == int:
            res[arg[i]] = i
        else:
            res[arg[i]].append(i)
    return res


def coincidence(arg1, arg2):
    res = []
    for i in range(len(arg1)):
        for j in range(len(arg2)):
            if arg1[i] == arg2[j]:
                res.append(arg1[i])

    return res


def count(arg):
    res = {}

    for i in range(len(arg)):
        res[arg[i]] = 0

    for i in range(len(arg)):
        res[arg[i]] += 1
    return res


def lensort(arg):
    argln = [len(x) for x in arg]
    ch = True
    while ch:
        ch = False
        for i in range(len(arg) - 1):
            if argln[i] > argln[i + 1]:
                argln[i], argln[i + 1] = argln[i + 1], argln[i]
                arg[i], arg[i + 1] = arg[i + 1], arg[i]
                ch = True
    return arg
