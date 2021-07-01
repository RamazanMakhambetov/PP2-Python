import sys
from collections import Counter

words = Counter(list(map(str, sys.stdin.read().split())))

def sortByAlphabet(inputStr):
    return inputStr[0]

list_values = list(words.items())
list_values.sort(key = sortByAlphabet)
list_values.sort(key = lambda i: i[1], reverse = True)

print(*[i for i, j in list_values])