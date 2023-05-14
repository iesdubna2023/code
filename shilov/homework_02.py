def reverse(arg):
    result = arg[::-1]
    return result


def avglen(arg):
    total_len = 0
    for i in arg:
        total_len += len(i)
    return total_len / len(arg)


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
    identical_elements = list(set(arg1) & set(arg2))
    return identical_elements


def count(arg):
    result = {}
    for i in arg:
        if arg.count(i) > 1:
            result[i] = arg.count(i)
        else:
            result[i] = 1
    return result


def lensort(arg):
    if len(arg) > 1:
        support_element = arg.pop()
        bigger_arg = []
        middle_arg = [support_element]
        smaller_arg = []
        for i in arg:
            if len(i) == len(support_element):
                middle_arg.append(i)
            elif len(i) > len(support_element):
                bigger_arg.append(i)
            else:
                smaller_arg.append(i)
        return lensort(smaller_arg) + middle_arg + lensort(bigger_arg)
    else:
        return arg
