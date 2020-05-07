import collections
import sys


def longest_substring(s, words):
    d = dict.fromkeys(words, 0)
    longest = ''
    for char in s:
        for w, i in d.items():
            # print(w, i)
            try:
                if char == w[i]:
                    d[w] += 1
            except IndexError:
                continue
            if d[w] == len(w):
                longest = max(longest, w, key=len)
    return longest


letters = "abbbpple"
words = ["able", "apple", "kangroo", "baleee", "lbaepp"]
print(longest_substring(letters, words))