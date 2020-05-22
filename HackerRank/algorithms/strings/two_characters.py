# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Strings: Two Characters
# problem url: https://www.hackerrank.com/challenges/two-characters/problem
# date: 05/21/2020

#!/bin/python3

def alternate(s):
    unic = sorted(list(set(s)))
    string_length = 0

    for index1 in range(len(unic)):
        for index2 in range(index1 + 1, len(unic)):
            lst = []
            for char in s:
                pair = {unic[index1], unic[index2]}
                char_in_pair = char in pair
                if char_in_pair:
                    if not lst or char != lst[-1]:
                        lst.append(char)
                    elif char == lst[-1]:
                        lst = []
                        break
            if len(lst) > string_length:
                string_length = len(lst)
    return string_length

input()
s = str(input())

print(int(alternate(s)))