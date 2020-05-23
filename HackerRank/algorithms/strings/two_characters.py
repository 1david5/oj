# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Strings: Two Characters
# problem url: https://www.hackerrank.com/challenges/two-characters/problem
# date: 05/21/2020

#!/bin/python3

def pair_substring(s, pair):
    substring = []
    for char in s:
        if char in pair:
            if not substring or char != substring[-1]:
                substring.append(char)
            elif char == substring[-1]:
                substring = []
                break
    return substring


def alternate(s):
    unic = sorted(list(set(s)))
    string_length = 0

    for index1 in range(len(unic)):
        for index2 in range(index1 + 1, len(unic)):
            pair = {unic[index1], unic[index2]}
            lst = pair_substring(s, pair)
            if len(lst) > string_length:
                string_length = len(lst)
    return string_length

input()
s = str(input())

print(int(alternate(s)))