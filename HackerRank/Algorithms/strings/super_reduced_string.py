# author: David Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Strings: Super Reduced String
# problem url: https://www.hackerrank.com/challenges/reduced-string/problem
# date: 05/20/2020

def superReducedString(s):
    l = []
    for i in range(len(s)):
        if l and s[i] == l[-1]:
            l.pop()
        else:
            l.append(s[i])
    if l:
        return "".join(l)
    else:
        return "Empty String"
