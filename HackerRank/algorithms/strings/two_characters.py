# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Strings: Two Characters
# problem url: https://www.hackerrank.com/challenges/two-characters/problem
# date: 05/21/2020

def alternate(s):
    unic = sorted(list(set(s)))
    m = []
    n = 0

    # Cretate matrix with possible character conbinations
    for i in range(len(unic)):
        for j in range(i + 1, len(unic)):
            m.append([unic[i], unic[j]])

    #Create possible lists with two alternating characteres and compare their lengths
    for pair in m:
        lst = []
        for char in s:
            if char in pair and not lst:
                lst.append(char)
                continue
            elif char in pair and char != lst[-1]:
                lst.append(char)
            elif char in pair and char == lst[-1]:
                lst = []
                break
        if len(lst) > n:
            n = len(lst)
    return n
