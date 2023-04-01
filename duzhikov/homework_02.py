def reverse(lst):
    return lst[::-1]


def avglen(lst):
    return sum(len(word) for word in lst) / len(lst)


def index(lst):
    result = {}
    for i in range(len(lst)):
        word = lst[i]
        if word not in result:
            result[word] = i
        else:
            if isinstance(result[word], list):
                result[word].append(i)
            else:
                result[word] = [result[word], i]
    return result


def coincidence(lst1, lst2):
    return list(set(lst1) & set(lst2))


def count(lst):
    result_dict = {}
    for word in lst:
        if word in result_dict:
            result_dict[word] += 1
        else:
            result_dict[word] = 1
    return result_dict


def lensort(lst):
    len_list = len(lst)
    for i in range(1, len_list):
        data = lst[i]
        c = i - 1
        while c >= 0 and len(data) < len(lst[c]):
            lst[c + 1] = lst[c]
            c -= 1
        lst[c + 1] = data
    return lst
