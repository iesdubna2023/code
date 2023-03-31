arg1 = ["my", "name", "is", "Masha"]
def question1(arg):
    return list(reversed(arg))




arg2 = ["a", "ab", "abc"]
def question2(arg):
    total_length = 0
    count = 0
    for word in arg:
        total_length += len(word)
        count += 1
    return total_length / count if count > 0 else 0




arg3 = ["her", "name", "is", "Masha", "Masha", "is", "a", "sister", "of", "Zhenya"]
def question3(arg):
    indexes = {}
    for i in range(len(arg)):
        word = arg[i]
        if word in indexes:
            indexes[word].append(i)
        else:
            indexes[word] = [i]
    return indexes




arg4_1 = ["my", "name", "is", "Masha"]
arg4_2 = ["my", "name", "is", "Zhenya"]
def question4(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))




arg5 = ["aaa", "aaa", "bbb", "ccc", "bbb"]
def question5(list):
    counts = {}
    for word in list:
        counts[word] = counts.get(word, 0) + 1
    return counts




arg6 = ["abcd", "a", "ab", "abc", "bazinga", "bar", '34,4']
def question6(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if len(list[i]) > len(list[j]):
                list[i], list[j] = list[j], list[i]
    return list




print(question1(arg1))
print(question2(arg2))
print(question3(arg3))
print(question4(arg4_1, arg4_2))
print(question5(arg5))
print(question6(arg6))