arg1 = ["my", "name", "is", "Masha"]
# result = ["Masha", "is", "name", "my"]
def reverse_list(lst):
    return lst[::-1]




arg2 = ["a", "ab", "abc"]
# result = 2.0
def average_word_length(lst):
    return sum(len(word) for word in lst) / len(lst)




arg3 = ["her", "name", "is", "Masha", "Masha", "is", "a", "sister", "of", "Zhenya"]
# result = {
#     "her": 0,
#     "name": 1,
#     "is": [2, 5],
#     "Masha": [3, 4],
#     "a": 6,
#     "sister": 7,
#     "of": 8,
#     "Zhenya": 9,
# }
from collections import defaultdict

def index_words(lst):
    indexes = defaultdict(list)
    for i, word in enumerate(lst):
        indexes[word].append(i)
    return {k: v[0] if len(v) == 1 else v for k, v in indexes.items()}




arg4_1 = ["my", "name", "is", "Masha"]
arg4_2 = ["my", "name", "is", "Zhenya"]
# result = ["my", "name", "is"]
def intersect_lists(lst1, lst2):
    return list(set(lst1) & set(lst2))




arg5 = ["aaa", "aaa", "bbb", "ccc", "bbb"]
# result = {
#     "aaa": 2,
#     "bbb": 2,
#     "ccc": 1,
# }
from collections import Counter

def count_words(lst):
    return dict(Counter(lst))




arg6 = ["abcd", "a", "ab", "abc", "bazinga", "bar"]
# result = ["a", "ab", "abc", "bar", "abcd", "bazinga"]
def sort_by_length(lst):
    return sorted(lst, key=len)




print(reverse_list(arg1))
print(average_word_length(arg2))
print(index_words(arg3))
print(intersect_lists(arg4_1, arg4_2))
print(count_words(arg5))
print(sort_by_length(arg6))