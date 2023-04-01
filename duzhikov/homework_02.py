from collections import defaultdict
from collections import Counter


def reverse(lst):
    return lst[::-1]


def avglen(lst):
    return sum(len(word) for word in lst) / len(lst)


def index(lst):
    indexes = defaultdict(list)
    for i, word in enumerate(lst):
        indexes[word].append(i)
    return {k: v[0] if len(v) == 1 else v for k, v in indexes.items()}


def coincidence(lst1, lst2):
    return list(set(lst1) & set(lst2))


def count(lst):
    return dict(Counter(lst))


def lensort(fix):
    len_list = len(fix)
    for i in range(1, len_list):
        data = fix[i]
        c = i - 1
        while c >= 0 and len(data) < len(fix[c]):
            fix[c + 1] = fix[c]
            c -= 1
        fix[c + 1] = data
    return fix
