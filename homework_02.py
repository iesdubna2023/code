arg1 = ["my", "name", "is", "Masha"]
def task1(list):
    reversed_lst = []
    for i in range(len(list) - 1, -1, -1):
        reversed_lst.append(list[i])
    return reversed_lst


arg2 = ["a", "ab", "abc"]
def task2(list):
    total_length = 0
    for word in list:
        total_length += len(word)
    return total_length / len(list)


arg3 = ["her", "name", "is", "Masha", "Masha", "is", "a", "sister", "of", "Zhenya"]
def task3(arg):
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


arg4_1 = ["my", "name", "is", "Masha"]
arg4_2 = ["my", "name", "is", "Zhenya"]
def task4(list1, list2):
    intersect = []
    for elem in list1:
        if elem in list2 and elem not in intersect:
            intersect.append(elem)
    return intersect


arg5 = ["aaa", "aaa", "bbb", "ccc", "bbb"]
def task5(list):
    counts = {}
    for word in list:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


arg6 = ["abcd", "a", "ab", "abc", "bazinga", "bar"]
def task6(list):
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



print(task1(arg1))
print(task2(arg2))
print(task3(arg3))
print(task4(arg4_1, arg4_2))
print(task5(arg5))
print(task6(arg6))