def reverse_list(lst):
    return lst[::-1]


def average_word_length(lst):
    return sum(len(word) for word in lst) / len(lst)


from collections import defaultdict

def index_words(lst):
    indexes = defaultdict(list)
    for i, word in enumerate(lst):
        indexes[word].append(i)
    return {k: v[0] if len(v) == 1 else v for k, v in indexes.items()}


def intersect_lists(lst1, lst2):
    return list(set(lst1) & set(lst2))


from collections import Counter

def count_words(lst):
    return dict(Counter(lst))


def sorted_by_Dimasik(list):
    len_list = len(list)
    for i in range(1, len_list):
        data = list[i]
        count = i - 1
        while count >= 0 and len(data) < len(list[count]):
            list[count + 1] = list[count]
            count -= 1
        list[count + 1] = data
    return (list)

