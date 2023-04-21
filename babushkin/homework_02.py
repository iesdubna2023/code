def reverse(list):
    reversed_lst = []
    for i in range(len(list) - 1, -1, -1):
        reversed_lst.append(list[i])
    return reversed_lst


def avglen(list):
    total_length = 0
    for word in list:
        total_length += len(word)
    return total_length / len(list)


def index(arg):
    indexes = {}
    for i, word in enumerate(arg):
        if word in indexes:
            if isinstance(indexes[word], list):
                indexes[word].append(i)
            else:
                indexes[word] = [indexes[word], i]
        else:
            indexes[word] = i
    return indexes


def coincidence(list1, list2):
    intersect = []
    for elem in list1:
        if elem in list2 and elem not in intersect:
            intersect.append(elem)
    return intersect


def count(list):
    counts = {}
    for word in list:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


def lensort(list):
    sorted_list = []
    for word in list:
        inserted = False
        for i in range(len(sorted_list)):
            if len(word) < len(sorted_list[i]):
                sorted_list.insert(i, word)
                inserted = True
                break
        if not inserted:
            sorted_list.append(word)
    return sorted_list
